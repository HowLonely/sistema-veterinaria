from django.contrib import admin
from django.urls import path
from veterinariaApi import views

urlpatterns = [
    path('razas/', views.raza_listado, name='razasListApi'),
    path('razas/<int:pk>/', views.raza_detalle, name='razasDetalleApi'),
    path('fichasclinicas/', views.fichaClinica_listado, name='fichasClinicasListApi'),
    path('fichasclinicas/<int:pk>/', views.fichaClinica_detalle, name='fichasClinicasDetalleApi'),
    path('atenciones/', views.atencion_listado, name='atencionesListApi'),
    path('atenciones/<int:pk>/', views.atencion_detalle, name='atencionesDetalleApi'),
    path('clientes/', views.cliente_listado, name='clientesListApi'),
    path('clientes/<int:pk>/', views.cliente_detalle, name='clientesDetalleApi'),
]
