from django.shortcuts import render
from django.http import HttpResponse

from veterinaria import models

# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

def clientes(req):
    data  = {
        'clientes': models.clientes,
        'mascotas': models.mascotas,
        'razas': models.razas,
    }
    return render(req, 'veterinaria/clientes.html', data)

def mascotas(req):
    data = {
        'mascotas': models.mascotas,
        'razas': models.razas,
        'clientes': models.clientes,
    }
    return render(req, 'veterinaria/mascotas.html', data)

def atenciones(req):
    data  = {
        'mascotas': models.mascotas,
        'atenciones': models.atenciones,
    }
    return render(req, 'veterinaria/atenciones.html', data)