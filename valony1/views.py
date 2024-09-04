from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hola mundo estas en el index de la aplicacion valony1")

def comienzo(request):
    return HttpResponse("hola binevenido a la segunda vista de la aplicacion")