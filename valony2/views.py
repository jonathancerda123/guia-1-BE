from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    html="""¡Hola! Bienvenido/a, esta es la página de inicio.
            <strong><a href="/valony2/estado">Siguiente</a></strong>
    """
    return HttpResponse(html)

def estado(request):
    html="""
    <h1>¿Cómo estás?</h1>
    <body>Espero que bien, ¡Ten un lindo día!</body>
    """
    return HttpResponse(html)