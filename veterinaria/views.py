from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import permission_required
from veterinaria import forms

from veterinaria import models

# Create your views here.
def inicio(req):
    return render(req, 'veterinaria/index.html')

# ================ CLIENTES =====================
@permission_required("veterinaria.view_cliente", raise_exception=True)
def clientes(req):
    if req.method == 'POST':
        form = forms.ClienteForm(req.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = forms.ClienteForm()
    return render(req, 'veterinaria/clientes.html', {'form': form, 'clientes': models.Cliente.objects.all(), 'mascotas': models.FichaClinica.objects.all(), 'razas': models.Raza.objects.all()})

@permission_required("veterinaria.view_cliente", raise_exception=True)
def ver_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)
    form = forms.ClienteForm(instance=cliente)

    return render(req, 'veterinaria/cliente.html', {'form': form, 'cliente': cliente})

@permission_required("veterinaria.change_cliente", raise_exception=True)
def editar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)

    if req.method == 'POST':
        form = forms.ClienteForm(req.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
        else:
            form = forms.ClienteForm(instance=cliente)
        return render(req, 'veterinaria/cliente.html', {'form': form, 'cliente': cliente})

@permission_required("veterinaria.delete_cliente", raise_exception=True)
def eliminar_cliente(req, cliente_id):
    cliente = get_object_or_404(models.Cliente, id=cliente_id)

    if req.method == 'POST':
        cliente.delete()
        return redirect('/clientes/')
        
    return render(req, 'veterinaria/clienteDel.html', {'cliente': cliente}) 


# ================ FICHAS CLINICAS =====================
@permission_required("veterinaria.view_fichaclinica", raise_exception=True)
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

@permission_required("veterinaria.view_fichaclinica", raise_exception=True)
def ver_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.FichaClinica, id=ficha_id)
    form = forms.FichaForm(instance=ficha_clinica)

    return render(req, 'veterinaria/ficha_clinica.html', {'form': form, 'ficha_clinica': ficha_clinica})

@permission_required("veterinaria.change_fichaclinica", raise_exception=True)
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

@permission_required("veterinaria.delete_fichaclinica", raise_exception=True)
def eliminar_ficha(req, ficha_id):
    ficha_clinica = get_object_or_404(models.FichaClinica, id=ficha_id)

    if req.method == 'POST':
        ficha_clinica.delete()
        return redirect('/fichas/')
        
    return render(req, 'veterinaria/ficha_clinicaDel.html', {'ficha_clinica': ficha_clinica})  


# ================ ATENCIONES =====================
@permission_required("veterinaria.view_atencion", raise_exception=True)
def atenciones(req):
    if req.method == 'POST':
        form = forms.AtencionForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect(req.path)
    else:
        form = forms.AtencionForm()
    return render(req, 'veterinaria/atenciones.html', {'form': form, 'atenciones': models.Atencion.objects.all() })

@permission_required("veterinaria.view_atencion", raise_exception=True)
def ver_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id=atencion_id)
    form = forms.AtencionForm(instance=atencion)

    return render(req, 'veterinaria/atencion.html', {'form': form, 'atencion': atencion})

@permission_required("veterinaria.change_atencion", raise_exception=True)
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

@permission_required("veterinaria.delete_atencion", raise_exception=True)
def eliminar_atencion(req, atencion_id):
    atencion = get_object_or_404(models.Atencion, id=atencion_id)

    if req.method == 'POST':
        atencion.delete()
        return redirect('/atenciones/')
        
    return render(req, 'veterinaria/atencionDel.html', {'atenciones': atencion})    

@permission_required("veterinaria.view_raza", raise_exception=True)
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

@permission_required("veterinaria.delete_raza", raise_exception=True)
def eliminar_raza(req, raza_id):
    raza = get_object_or_404(models.Raza, id=raza_id)
    raza.delete()
    return redirect('/razas/')

@permission_required("veterinaria.view_raza", raise_exception=True)
def raza(req, raza_id):
    raza = get_object_or_404(models.Raza, id=raza_id)
    if req.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = forms.RazaForm(instance=raza)
        return HttpResponse(form.as_div())

@permission_required("veterinaria.change_raza", raise_exception=True)
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