from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    return HttpResponse("¡Hola! Bienvenido/a esta es la página de inicio.")