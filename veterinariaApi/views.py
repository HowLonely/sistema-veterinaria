from django.shortcuts import render
from veterinaria.models import Raza, FichaClinica, Atencion, Cliente
from django.http import JsonResponse
from veterinariaApi.serializers import RazaSerializar, FichaClinicaSerializar, AtencionSerializar, ClienteSerializar
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import permission_required

@permission_required("veterinaria.view_raza", raise_exception=True)
@api_view(['GET', 'POST'])
def raza_listado(req):
    if req.method == 'GET':
        razas = Raza.objects.all()
        serializer = RazaSerializar(razas, many=True)
        return Response(serializer.data)
    
    if req.method == 'POST':
        serializer = RazaSerializar(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_required("veterinaria.change_raza", raise_exception=True)
@permission_required("veterinaria.delete_raza", raise_exception=True)
@permission_required("veterinaria.view_raza", raise_exception=True)
@api_view(['GET', 'PUT', 'DELETE'])
def raza_detalle(req, pk):
    try:
        raza = Raza.objects.get(id=pk)
    except Raza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = RazaSerializar(raza)
        return Response(serializer.data)

    if req.method == 'PUT':
        serializer = RazaSerializar(raza,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'DELETE':
        raza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_required("veterinaria.view_fichaclinica", raise_exception=True)
@api_view(['GET', 'POST'])
def fichaClinica_listado(req):
    if req.method == 'GET':
        fichas_clinicas = FichaClinica.objects.all()
        serializer = FichaClinicaSerializar(fichas_clinicas, many=True)
        return Response(serializer.data)
    
    if req.method == 'POST':
        serializer = FichaClinicaSerializar(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_required("veterinaria.change_fichaclinica", raise_exception=True)
@permission_required("veterinaria.delete_fichaclinica", raise_exception=True)
@permission_required("veterinaria.view_fichaclinica", raise_exception=True)
@api_view(['GET', 'PUT', 'DELETE'])
def fichaClinica_detalle(req, pk):
    try:
        ficha_clinica = FichaClinica.objects.get(id=pk)
    except FichaClinica.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = FichaClinicaSerializar(ficha_clinica)
        return Response(serializer.data)

    if req.method == 'PUT':
        serializer = FichaClinicaSerializar(ficha_clinica,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'DELETE':
        ficha_clinica.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_required("veterinaria.view_atencion", raise_exception=True)
@api_view(['GET', 'POST'])
def atencion_listado(req):
    if req.method == 'GET':
        atenciones = Atencion.objects.all()
        serializer = AtencionSerializar(atenciones, many=True)
        return Response(serializer.data)
    
    if req.method == 'POST':
        serializer = AtencionSerializar(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_required("veterinaria.change_atencion", raise_exception=True)
@permission_required("veterinaria.delete_atencion", raise_exception=True)
@permission_required("veterinaria.view_atencion", raise_exception=True)
@api_view(['GET', 'PUT', 'DELETE'])
def atencion_detalle(req, pk):
    try:
        atencion = Atencion.objects.get(id=pk)
    except Atencion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = AtencionSerializar(atencion)
        return Response(serializer.data)

    if req.method == 'PUT':
        serializer = AtencionSerializar(atencion,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'DELETE':
        atencion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_required("veterinaria.view_cliente", raise_exception=True)
@api_view(['GET', 'POST'])
def cliente_listado(req):
    if req.method == 'GET':
        clientes = Cliente.objects.all()
        serializer = ClienteSerializar(clientes, many=True)
        return Response(serializer.data)
    
    if req.method == 'POST':
        serializer = ClienteSerializar(data = req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@permission_required("veterinaria.change_cliente", raise_exception=True)
@permission_required("veterinaria.delete_cliente", raise_exception=True)
@permission_required("veterinaria.view_cliente", raise_exception=True)
@api_view(['GET', 'PUT', 'DELETE'])
def cliente_detalle(req, pk):
    try:
        cliente = Cliente.objects.get(id=pk)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'GET':
        serializer = ClienteSerializar(cliente)
        return Response(serializer.data)

    if req.method == 'PUT':
        serializer = ClienteSerializar(cliente,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    if req.method == 'DELETE':
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
