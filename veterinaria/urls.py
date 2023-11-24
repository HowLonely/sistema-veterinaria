from django.contrib import admin
from django.urls import path
from veterinaria import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('clientes/', views.clientes, name='clientes'),
    path('cliente/<int:cliente_id>/', views.ver_cliente, name='verCliente'),
    path('clienteEdit/<int:cliente_id>/', views.editar_cliente, name='clienteEdit'),
    path('clienteDel/<int:cliente_id>/', views.eliminar_cliente, name='clienteDel'),

    path('fichas/', views.fichas, name='fichas'),
    path('ficha/<int:ficha_id>/', views.ver_ficha, name='verFicha'),
    path('fichaEdit/<int:ficha_id>/', views.editar_ficha, name='fichaEdit'),
    path('fichaDel/<int:ficha_id>/', views.eliminar_ficha, name='fichaDel'),
    
    path('atenciones/', views.atenciones, name='atenciones'),
    path('atencion/<int:atencion_id>/', views.ver_atencion, name='verAtencion'),
    path('atencionEdit/<int:atencion_id>/', views.editar_atencion, name='atencionEdit'),
    path('atencionDel/<int:atencion_id>/', views.eliminar_atencion, name='atencionDel'),
    # path('clienteAdd/', views.crear_cliente, name='crearCliente'),

    path('razas/', views.razas, name='razas'),
    path('eliminar_raza/<int:raza_id>/', views.eliminar_raza, name='eliminar_raza'),
    path('modificar_raza/<int:raza_id>/', views.modificar_raza, name='modificar_raza'),
]
