from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from django.http.request import HttpRequest
from django.http import Http404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from rest_framework.authtoken.views import obtain_auth_token,Token
from django.http import JsonResponse





from signup.models import Account, Notes, Tag
from .serializers import AccountSerializer, TagSerializer, NotesSerializer

from django.http import HttpResponse

class SignUP(APIView):
    permissions_classes = [IsAuthenticated]


    def index(request):
        return HttpResponse("Olá mundo! Este é um sistema de Login chamado SignUp.")


    @api_view(['GET', 'POST','DELETE','PUT'])
    def api_account(request, account_id=None):
        if request.method == 'GET':
            # permissions_classes = [IsAuthenticated,]
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                raise Http404()
        
        # if request.method == 'POST':
        #     #Creating User
        #     user = User.objects.create_user(request.data['username'],request.data['email'],request.data['password'])
            
        #     user.save()

        #     #Creating Account

        #     account = Account()
        #     new_account = request.data
        #     account.user = user
        #     account.name = new_account['name']
        #     account.age = new_account['age']

        #     account.save()
        
        if request.method == "DELETE":
            # permissions_classes = [IsAuthenticated,]
            try:
                account = Account.objects.get(id=account_id)
            except Account.DoesNotExist:
                return HttpResponse('Vish. Parece que já não existia esse conta mesmo. Aparentemente, a Lei de Murphy trabalhou a seu favor.')
            
            account.delete()

            account = Account()
        
        if request.method == "PUT":
            # permissions_classes = [IsAuthenticated,]
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
                account.user.email = updated_account['email']
            
            
            account.save()

            
        serialized_account = AccountSerializer(account)
        return Response(serialized_account.data)

    @api_view(['GET'])
    def api_accounts(request):
        if request.method == 'GET':
            # permissions_classes = [IsAuthenticated,]
            
        
            accounts = Account.objects.all()
        
        accounts_serializer = AccountSerializer(accounts,many=True)
            
        return Response(accounts_serializer.data)
    
        '''
        retorna todas as tags de um usuário
    '''
    @api_view(['GET'])

    def api_account_tags_get(request, account_name):
        if request.method == 'GET':
            tags = []
            accountUser = Account.objects.get(name = account_name)
            notes = Notes.objects.filter(account = accountUser)

            for note in notes:
                tags.append(note.tag)
            
        tags_serializer = TagSerializer(tags,many=True)
        return Response(tags_serializer.data)


    '''
        retorna as notas de um usuário
    '''
    @api_view(['GET'])

    def api_account_notes_get(request, account_name):
        if request.method == 'GET':
        
            accountUser = Account.objects.get(name = account_name)
            notes = Notes.objects.filter(account = accountUser)
        
        notes_serializer = NotesSerializer(notes,many=True)
            
        return Response(notes_serializer.data)

    '''
        faz o post de uma nota na conta de um usuário (funcionando)
    '''
    @api_view(['POST'])
    def api_account_note_post(request, account_name):
        if request.method == 'POST':
            accountUser = Account.objects.get(name = account_name)
            
            
            tag_note = Tag(tag = request.data['tag'])
            tag_note.save()
            
            titulo = request.data['title']
            conteudo = request.data['content']
            usuario = accountUser
            note = Notes(title = titulo, content=conteudo, account=usuario, tag=tag_note)
            note.save()
            
        note_serializer = NotesSerializer(note)
        return Response(note_serializer.data)
        
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create(request):
    if request.method == 'POST':
        #Creating User
        user = User.objects.create_user(request.data['username'],request.data['email'],request.data['password'])
        
        user.save()

        #Creating Account

        account = Account()
        new_account = request.data
        account.user = user
        account.name = new_account['name']
        account.age = new_account['age']

        account.save()

        token = Token.objects.create(user=user)
        Token_json = {"Token":str(token)}
    serialized_account = AccountSerializer(account)
    return JsonResponse(Token_json)



