from django.contrib import admin

# Register your models here.
from veterinaria.models import CustomUser, TipoUsuario, Atencion, Cliente, FichaClinica, Raza

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('rut','cod_profesional','id_tipo_usuario','username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)