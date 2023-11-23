from django.contrib import admin

# Register your models here.
from veterinaria.models import CustomUser, TipoUsuario, Atencion, Cliente, FichaClinica, Raza

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'rut','cod_profesional','id_tipo_usuario','username', 'email', 'first_name', 'last_name', 'is_staff')

class TipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'rol']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'rut', 'nombres', 'apellidos', 'fono_1', 'fono_2', 'email']

class RazaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_raza', 'nombre_especie']

class FichaClinicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_mascota', 'num_chip', 'edad_meses', 'sexo', 'imagen', 'id_raza', 'id_cliente']

class AtencionAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_mascota', 'hora_ingreso', 'hora_termino', 'diagnostico', 'tratamiento', 'observaciones', 'fecha_atencion', 'id_veterinario']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TipoUsuario, TipoUsuarioAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Raza, RazaAdmin)
admin.site.register(FichaClinica, FichaClinicaAdmin)
admin.site.register(Atencion, AtencionAdmin)