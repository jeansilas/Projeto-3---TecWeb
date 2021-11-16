from django.shortcuts import render, HttpResponse

#from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá mundo! Este é um sistema de Login chamado SignUp.")
