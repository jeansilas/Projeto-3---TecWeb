from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import Http404

from signup.models import Account
from .serializers import AccountSerializer

from django.http import HttpResponse

class SignUP(APIView):
    permissions = [IsAuthenticated,]
    def index(request):
        return HttpResponse("Olá mundo! Este é um sistema de Login chamado SignUp.")


    @api_view(['GET', 'POST','DELETE','PUT'])
    def api_account(request, account_id=None):
        if request.method == 'GET':
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                raise Http404()
        
        if request.method == 'POST':
            account = Account()
            new_account = request.data
            account.name = new_account['name']
            account.content = new_account['content']
            account.age = new_account['age']
            account.email = new_account['email']
            account.save()
        
        if request.method == "DELETE":
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse('Vish. Parece que já não existia esse conta mesmo. Aparentemente, a Lei de Murphy trabalhou a seu favor.')
            
            account.delete()

            account = Account()
        
        if request.method == "PUT":
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse('Vish. Parece que dessa vez, a Lei de Murphy não trabalhou a seu favor.')
            
            updated_account = request.data

            #Updating name
            if updated_account['name'] != "" and updated_account['name'] != None:
                account.name = updated_account['name']

            #Updating age
            if str(updated_account['age']) != "" and str(updated_account['age']) != None:
                account.age = updated_account['age']
            
            #Updating email
            if updated_account['email'] != "" and updated_account['email'] != None:
                account.email = updated_account['email']
            
            #Updating content
            if updated_account['content'] != "" and updated_account['content'] != None:
                account.content = updated_account['content']
            
            account.save()

            
        serialized_account = AccountSerializer(account)
        return Response(serialized_account.data)

    @api_view(['GET'])
    def api_accounts(request):
        if request.method == 'GET':
            
        
            accounts = Account.objects.all()
        
        accounts_serializer = AccountSerializer(accounts,many=True)
            
        return Response(accounts_serializer.data)


