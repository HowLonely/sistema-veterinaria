from django.utils import timezone
from django.db import models
import os
from django.contrib.auth.models import AbstractUser

class TipoUsuario(models.Model):
    rol = models.CharField(max_length=95)
    def __str__(self):
        return self.rol

class CustomUser(AbstractUser):
    rut = models.CharField(max_length=10)
    cod_profesional = models.CharField(max_length=45, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        # Hasheamos la contraseña antes de guardar
        if self.password:
            self.set_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Raza(models.Model):
    nombre_raza = models.CharField(max_length=145)
    nombre_especie = models.CharField(max_length=145)

    def __str__(self):
        return self.nombre_raza

class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=145)
    apellidos = models.CharField(max_length=145)
    fono_1 = models.IntegerField(null=True)
    fono_2 = models.IntegerField(null=True)
    email = models.CharField(max_length=245, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class FichaClinica(models.Model):
    nombre_mascota = models.CharField(max_length=95)
    num_chip = models.CharField(max_length=145, null=True)
    edad_meses = models.IntegerField(null=True)
    sexo = models.BooleanField(null=True)

    def generarRuta(instance, filename):
        extension = os.path.splitext(filename)[1][1:]
        ruta = 'mascotas'
        fecha = timezone.now().strftime("%d%m%Y_%H%M%S")
        nombre = "{}.{}".format(fecha, extension)
        return os.path.join(ruta, nombre)
    
    imagen = models.ImageField(upload_to=generarRuta, null=True, default='mascotas/mascota.png')
    id_raza = models.ForeignKey(Raza, on_delete=models.CASCADE, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre_mascota



class Atencion(models.Model):
    id_mascota = models.ForeignKey(FichaClinica, on_delete=models.CASCADE, null=True)
    hora_ingreso = models.TimeField(null=True)
    hora_termino = models.TimeField(null=True)
    diagnostico = models.CharField(max_length=245, null=True)
    tratamiento = models.CharField(max_length=145, null=True)
    observaciones = models.CharField(max_length=245, null=True)
    fecha_atencion = models.DateField(null=True)
    id_veterinario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    id_mascota = models.ForeignKey(FichaClinica, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Atencion {self.id_atencion}"
