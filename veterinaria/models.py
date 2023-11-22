from django.db import models

class TipoUsuario(models.Model):
    rol = models.CharField(max_length=95)

    def __str__(self):
        return self.rol

class Usuario(models.Model):
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=145)
    apellidos = models.CharField(max_length=145)
    cod_profesional = models.CharField(max_length=45, null=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, null=True)
    fono_1 = models.IntegerField(null=True)
    email = models.CharField(max_length=245, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

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

class Mascota(models.Model):
    nombre_mascota = models.CharField(max_length=95)
    num_chip = models.CharField(max_length=145, null=True)
    edad_meses = models.IntegerField(null=True)
    sexo = models.BooleanField(null=True)
    url_imagen = models.CharField(max_length=145, null=True)
    id_raza = models.ForeignKey(Raza, on_delete=models.CASCADE, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre_mascota

class Atencion(models.Model):
    id_mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True)
    hora_ingreso = models.TimeField(null=True)
    hora_termino = models.TimeField(null=True)
    diagnostico = models.CharField(max_length=245, null=True)
    tratamiento = models.CharField(max_length=145, null=True)
    observaciones = models.CharField(max_length=245, null=True)
    fecha_atencion = models.DateField(null=True)
    id_veterinario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Atencion {self.id_atencion}"
