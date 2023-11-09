from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from veterinaria import forms

from veterinaria import models

# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

def clientes(req):
    if req.method == 'POST':
        form = forms.ClienteForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(req.path)
    else:
        form = forms.ClienteForm
    
    return render(req, 'veterinaria/clientes.html', {'form': form, 'clientes': models.Clientes.objects.all(), 'mascotas': models.Mascotas.objects.all(), 'razas': models.Razas.objects.all()})

def ver_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Clientes, id_cliente=cliente_id)
    form = forms.ClienteForm(instance=cliente)

    return render(req, 'veterinaria/cliente.html', {'form': form, 'cliente': cliente})

def editar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Clientes, id_cliente=cliente_id)

    if req.method == 'POST':
        form = forms.ClienteForm(req.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
        else:
            form = forms.ClienteForm(instance=cliente)
        return render(req, 'veterinaria/cliente.html', {'form': form})

def eliminar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Clientes, id_cliente=cliente_id)

    if req.method == 'POST':
        cliente.delete()
        return redirect('/clientes/')
        
    return render(req, 'veterinaria/clienteDel.html', {'cliente': cliente}) 

def mascotas(req):
    data = {
        'mascotas': models.Mascotas.objects.all(),
        'razas': models.Razas.objects.all(),
        'clientes': models.Clientes.objects.all(),
    }
    return render(req, 'veterinaria/mascotas.html', data)

def atenciones(req):
    if req.method == 'POST':
        form = forms.AtencionForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(req.path)
    else:
        form = forms.AtencionForm()
    return render(req, 'veterinaria/atenciones.html', {'form': form, 'atenciones': models.Atenciones.objects.all() })

def ver_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atenciones, id_atencion=atencion_id)
    form = forms.AtencionForm(instance=atencion)

    return render(req, 'veterinaria/atencion.html', {'form': form, 'atencion': atencion})

def editar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atenciones, id_atencion=atencion_id)

    if req.method == 'POST':
        form = forms.AtencionForm(req.POST, instance=atencion)
        if form.is_valid():
            form.save()
            return redirect('/atenciones/')
    else:
        form = forms.AtencionForm(instance=atencion)
    return render(req, 'veterinaria/atencion.html', {'form': form})

def eliminar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atenciones, id_atencion=atencion_id)

    if req.method == 'POST':
        atencion.delete()
        return redirect('/atenciones/')
        
    return render(req, 'veterinaria/atencionDel.html', {'atenciones': atencion})    

