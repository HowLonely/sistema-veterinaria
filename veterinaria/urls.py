from django.contrib import admin
from django.urls import path
from veterinaria import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('clientes/', views.clientes, name='clientes'),
]
