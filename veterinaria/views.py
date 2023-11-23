from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from veterinaria import forms

from veterinaria import models

# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

# ================ CLIENTES =====================
def clientes(req):
    if req.method == 'POST':
        form = forms.ClienteForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(req.path)
    else:
        form = forms.ClienteForm
    
    return render(req, 'veterinaria/clientes.html', {'form': form, 'clientes': models.Cliente.objects.all(), 'mascotas': models.Ficha_clinica.objects.all(), 'razas': models.Raza.objects.all()})

def ver_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id_cliente=cliente_id)
    form = forms.ClienteForm(instance=cliente)

    return render(req, 'veterinaria/cliente.html', {'form': form, 'cliente': cliente})

def editar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id_cliente=cliente_id)

    if req.method == 'POST':
        form = forms.ClienteForm(req.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
        else:
            form = forms.ClienteForm(instance=cliente)
        return render(req, 'veterinaria/cliente.html', {'form': form})

def eliminar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id_cliente=cliente_id)

    if req.method == 'POST':
        cliente.delete()
        return redirect('/clientes/')
        
    return render(req, 'veterinaria/clienteDel.html', {'cliente': cliente}) 


# ================ FICHAS CLINICAS =====================
def fichas(req):
    data = {
        'fichas': models.Ficha_clinica.objects.all(),
        'razas': models.Raza.objects.all(),
        'clientes': models.Cliente.objects.all(),
    }
    return render(req, 'veterinaria/fichas_clinicas.html', data)

def ver_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.Ficha_clinica, id_ficha=ficha_id)
    form = forms.AtencionForm(instance=ficha_clinica)

    return render(req, 'veterinaria/ficha_clinica.html', {'form': form, 'ficha_clinica': ficha_clinica})

def editar_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.Ficha_clinica, id_atencion=ficha_id)

    if req.method == 'POST':
        form = forms.FichaForm(req.POST, instance=ficha_clinica)
        if form.is_valid():
            form.save()
            return redirect('/fichas_clinicas/')
    else:
        form = forms.FichaForm(instance=ficha_clinica)
    return render(req, 'veterinaria/ficha_clinica.html', {'form': form})

def eliminar_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.Ficha_clinica, id_ficha=ficha_id)

    if req.method == 'POST':
        ficha_clinica.delete()
        return redirect('/fichas_clinicas/')
        
    return render(req, 'veterinaria/ficha_clinicaDel.html', {'ficha_clinica': ficha_clinica})  


# ================ ATENCIONES =====================
def atenciones(req):
    if req.method == 'POST':
        form = forms.AtencionForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(req.path)
    else:
        form = forms.AtencionForm()
    return render(req, 'veterinaria/atenciones.html', {'form': form, 'atenciones': models.Atencion.objects.all() })

def ver_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id_atencion=atencion_id)
    form = forms.AtencionForm(instance=atencion)

    return render(req, 'veterinaria/atencion.html', {'form': form, 'atencion': atencion})

def editar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id_atencion=atencion_id)

    if req.method == 'POST':
        form = forms.AtencionForm(req.POST, instance=atencion)
        if form.is_valid():
            form.save()
            return redirect('/atenciones/')
    else:
        form = forms.AtencionForm(instance=atencion)
    return render(req, 'veterinaria/atencion.html', {'form': form})

def eliminar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id_atencion=atencion_id)

    if req.method == 'POST':
        atencion.delete()
        return redirect('/atenciones/')
        
    return render(req, 'veterinaria/atencionDel.html', {'atenciones': atencion})    

def razas(req):
    return render(req, 'veterinaria/especies.html', { 'razas': models.Raza.objects.all(), 'mascotas': models.Ficha_clinica.objects.all() })