from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
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
    
    return render(req, 'veterinaria/clientes.html', {'form': form, 'clientes': models.Cliente.objects.all(), 'mascotas': models.FichaClinica.objects.all(), 'razas': models.Raza.objects.all()})

def ver_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)
    form = forms.ClienteForm(instance=cliente)

    return render(req, 'veterinaria/cliente.html', {'form': form, 'cliente': cliente})

def editar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)

    if req.method == 'POST':
        form = forms.ClienteForm(req.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
        else:
            form = forms.ClienteForm(instance=cliente)
        return render(req, 'veterinaria/cliente.html', {'form': form})

def eliminar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)

    if req.method == 'POST':
        cliente.delete()
        return redirect('/clientes/')
        
    return render(req, 'veterinaria/clienteDel.html', {'cliente': cliente}) 


# ================ FICHAS CLINICAS =====================
def fichas(req):
    if req.method == 'POST':
        form = forms.FichaForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = forms.FichaForm()
    return render(req, 'veterinaria/fichas_clinicas.html', {'form': form,'fichas': models.FichaClinica.objects.all(), 'razas': models.Raza.objects.all(), 'clientes': models.Cliente.objects.all()})

def ver_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.FichaClinica, id=ficha_id)
    form = forms.FichaForm(instance=ficha_clinica)

    return render(req, 'veterinaria/ficha_clinica.html', {'form': form, 'ficha_clinica': ficha_clinica})

def editar_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.FichaClinica, id=ficha_id)

    if req.method == 'POST':
        form = forms.FichaForm(req.POST, req.FILES, instance=ficha_clinica)
        if form.is_valid():
            if 'imagen' in req.FILES:
                ficha_clinica.imagen = req.FILES['imagen']
            form.save()
            return redirect('/fichas/')
    else:
        form = forms.FichaForm(instance=ficha_clinica)
    return render(req, 'veterinaria/ficha_clinica.html', {'form': form})

def eliminar_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.FichaClinica, id=ficha_id)

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
    atencion = get_object_or_404(models.Atencion, id=atencion_id)
    form = forms.AtencionForm(instance=atencion)

    return render(req, 'veterinaria/atencion.html', {'form': form, 'atencion': atencion})

def editar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id=atencion_id)

    if req.method == 'POST':
        form = forms.AtencionForm(req.POST, instance=atencion)
        if form.is_valid():
            form.save()
            return redirect('/atenciones/')
    else:
        form = forms.AtencionForm(instance=atencion)
    return render(req, 'veterinaria/atencion.html', {'form': form})

def eliminar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id=atencion_id)

    if req.method == 'POST':
        atencion.delete()
        return redirect('/atenciones/')
        
    return render(req, 'veterinaria/atencionDel.html', {'atenciones': atencion})    

def razas(req):
    if req.method == 'POST':
        form = forms.RazaForm(req.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = forms.RazaForm()
    return render(req, 'veterinaria/especies.html', { 'form': form, 'razas': models.Raza.objects.all(), 'mascotas': models.FichaClinica.objects.all() })

def eliminar_raza(req, raza_id):
    raza = get_object_or_404(models.Raza, id=raza_id)
    raza.delete()
    return redirect('/razas/')

def modificar_raza(req, raza_id):
    raza = get_object_or_404(models.Raza, id=raza_id)
    if req.method == 'POST':
        form = forms.RazaForm(req.POST, instance=raza)
        if form.is_valid():
            form.save()
            return redirect('/razas/')
    else:
        form = forms.RazaForm(instance=raza)
    return render(req, 'veterinaria/especies.html', { 'form': form, 'razas': models.Raza.objects.all(), 'mascotas': models.FichaClinica.objects.all() })