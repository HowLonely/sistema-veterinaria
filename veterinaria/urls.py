from django.contrib import admin
from django.urls import path
from veterinaria import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('clientes/', views.clientes, name='clientes'),
    path('cliente/<int:cliente_id>/', views.ver_cliente, name='verCliente'),
    path('clienteEdit/<int:cliente_id>/', views.editar_cliente, name='clienteEdit'),
    path('clienteDel/<int:cliente_id>/', views.eliminar_cliente, name='clienteDel'),

    path('mascotas/', views.mascotas, name='mascotas'),
    
    path('atenciones/', views.atenciones, name='atenciones'),
    path('atencion/<int:atencion_id>/', views.ver_atencion, name='verAtencion'),
    path('atencionEdit/<int:atencion_id>/', views.editar_atencion, name='atencionEdit'),
    path('atencionDel/<int:atencion_id>/', views.eliminar_atencion, name='atencionDel'),
    # path('clienteAdd/', views.crear_cliente, name='crearCliente'),
]
