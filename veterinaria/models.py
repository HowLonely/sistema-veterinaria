from django.db import models

# Create your models here.
clientes = [
    {'rut': '18789374-1', 'nombre': 'pedro', 'apellidos': 'diaz rojas', 'fono_1': '932384983', 'fono_2': '923784732', 'email': 'pedro.dr@correo.cl'},
    {'rut': '17389832-2', 'nombre': 'juan', 'apellidos': 'toledo gonzalez', 'fono_1': '912893829', 'fono_2': '912832928', 'email': 'juan.tg@correo.cl'},
    {'rut': '19239843-1', 'nombre': 'camila', 'apellidos': 'vargas salazar', 'fono_1': '932387645', 'fono_2': '966476663', 'email': 'camila.vs@correo.cl'},
]
# Foreign key son las posiciones en los arreglos. ej: raza:0 -> razas[0]
razas = [
    {'nombre_raza': 'pastor aleman', 'especie': 'perro'},
    {'nombre_raza': 'angora', 'especie' : 'gato'},
    {'nombre_raza': 'loro gris africano', 'especie': 'loro'},
]

mascotas = [
    {'sexo': 0, 'edad_meses': 54, 'nombre': 'blanca', 'num_chip': 120030, 'raza': razas[0], 'dueno': clientes[0]},
    {'sexo': 1, 'edad_meses': 24, 'nombre': 'negro', 'num_chip': 100293, 'raza': razas[1], 'dueno': clientes[2]},
    {'sexo': 1, 'edad_meses': 75, 'nombre': 'homero', 'num_chip': None, 'raza': razas[2], 'dueno': clientes[1]},
]

veterinarios = [
    # rut, credencial, nombre, apellidos, fono, email
]

fichas_clinicas = [
    {'mascota': mascotas[0], 'veterinario': veterinarios[0]}
]

atenciones = [
    {'cod_atencion': 123, 'hora_inicio': '12:15', 'hora_termino': '13:00', 'veterinario': 'Snoop Dogg', 'fecha_atencion': '15/09/2023','mascota_atendida': mascotas[0] , 'diagnostico': 'Enfermedad por estrés', 'tratamiento': 'Acostarse mas temprano','observaciones': None, 'fechas_control': '02/10/2023'},
    {'cod_atencion': 456, 'hora_inicio': '10:30', 'hora_termino': '11:00', 'veterinario': 'Bad Bunny', 'fecha_atencion': '10/08/2023','mascota_atendida': mascotas[1],'diagnostico': 'Pie plano', 'tratamiento': 'Reposo','observaciones': 'Evitar esfuerzo fisico', 'fechas_control': '06/09/2023'},
    {'cod_atencion': 789, 'hora_inicio': '15:00', 'hora_termino': '15:15', 'veterinario': 'Pablo Chill-E', 'fecha_atencion': '15/09/2023','mascota_atendida': mascotas[2], 'diagnostico': 'Irritación en el ojo', 'tratamiento': 'Gotas para los ojos a diario','observaciones': 'Evitar estar en ambientes áridos', 'fechas_control': '30/09/2023'},
]