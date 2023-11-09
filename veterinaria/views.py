from django.shortcuts import render
from django.http import HttpResponse

from veterinaria import models

# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

def clientes(req):
    data  = {
        'clientes': models.Clientes.objects.all(),
        'mascotas': models.Mascotas.objects.all(),
        'razas': models.Razas.objects.all(),
    }
    return render(req, 'veterinaria/clientes.html', data)

def mascotas(req):
    data = {
        'mascotas': models.Mascotas.objects.all(),
        'razas': models.Razas.objects.all(),
        'clientes': models.Clientes.objects.all(),
    }
    return render(req, 'veterinaria/mascotas.html', data)

def atenciones(req):
    data  = {
        'mascotas': models.Mascotas,
        'atenciones': models.Atenciones,
    }
    return render(req, 'veterinaria/atenciones.html', data)