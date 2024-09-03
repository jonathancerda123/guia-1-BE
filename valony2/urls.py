from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenida), #la primera parte es el enlace.
    path('estado/', views.estado),
]