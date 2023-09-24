from django.shortcuts import render
from django.http import HttpResponse

from veterinaria import models
# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

def clientes(req):
    return render(req, 'veterinaria/clientes.html', models.clientes)