from django.shortcuts import render, redirect
from django.http import HttpResponse
from veterinaria import forms

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
        'atenciones': models.Atenciones.objects.all(),
    }
    return render(req, 'veterinaria/atenciones.html', data)

def crear_cliente(req):
    if req.method == 'POST':
        form = forms.ClienteForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinaria/clientes.html')
    else:
        form = forms.ClienteForm
    
    return render(req, 'veterinaria/clienteAdd.html', {'form': form})