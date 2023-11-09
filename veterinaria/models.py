# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistentes(models.Model):
    id_asistente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=145, blank=True, null=True)
    apellidos = models.CharField(max_length=145, blank=True, null=True)
    fono = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=245, blank=True, null=True)
    credenciales = models.CharField(max_length=145, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

    class Meta:
        managed = False
        db_table = 'asistentes'


class Atenciones(models.Model):
    id_atencion = models.AutoField(primary_key=True, editable=False, blank=True)
    hora_ingreso = models.TimeField(blank=True, null=True)
    hora_termino = models.TimeField(blank=True, null=True)
    id_ficha_clinica = models.ForeignKey('FichasClinicas', models.DO_NOTHING, db_column='id_ficha_clinica', blank=True, null=True)
    id_veterinario = models.ForeignKey('Veterinarios', models.DO_NOTHING, db_column='id_veterinario', blank=True, null=True)
    diagnostico = models.CharField(max_length=280, blank=True, null=True)
    tratamiento = models.CharField(max_length=280, blank=True, null=True)
    observaciones = models.CharField(max_length=245, blank=True, null=True)
    fecha_atencion = models.DateField(blank=True, null=True)
    agendada_por_asistente = models.ForeignKey(Asistentes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atenciones'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10, blank=True, null=True)
    nombres = models.CharField(max_length=145, blank=True, null=True)
    apellidos = models.CharField(max_length=145, blank=True, null=True)
    fono_1 = models.CharField(max_length=14, blank=True, null=True)
    fono_2 = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class FichasClinicas(models.Model):
    id_ficha_clinica = models.AutoField(primary_key=True)
    id_mascota = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='id_mascota', blank=True, null=True)
    id_veterinario = models.ForeignKey('Veterinarios', models.DO_NOTHING, db_column='id_veterinario', blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    creada_por_asistente = models.ForeignKey(Asistentes, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.id_mascota.nombres, self.id_mascota.num_chip)

    class Meta:
        managed = False
        db_table = 'fichas_clinicas'


class Mascotas(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    id_dueno = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_dueno', blank=True, null=True)
    nombres = models.CharField(max_length=145, blank=True, null=True)
    num_chip = models.CharField(max_length=145, blank=True, null=True)
    id_raza = models.ForeignKey('Razas', models.DO_NOTHING, db_column='id_raza', blank=True, null=True)
    edad_meses = models.IntegerField(blank=True, null=True)
    sexo = models.IntegerField(blank=True, null=True)
    url_imagen = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mascotas'


class Razas(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=85, blank=True, null=True)
    nombre_especie = models.CharField(max_length=85, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'razas'


class Veterinarios(models.Model):
    id_veterinario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=145, blank=True, null=True)
    apellidos = models.CharField(max_length=145, blank=True, null=True)
    credenciales = models.CharField(max_length=145, blank=True, null=True)
    fono = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=245, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

    class Meta:
        managed = False
        db_table = 'veterinarios'
