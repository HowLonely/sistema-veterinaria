from django.db import models

# Create your models here.
clientes = {
    # rut, nombre, apellidos, fono_1, fono_2, email
    0:['18789374-1', 'pedro', 'diaz rojas', '932384983', '923784732', 'pedro.dr@correo.cl'],
    1:['17389832-2', 'juan', 'toledo gonzalez', '912893829', '912832928', 'juan.tg@correo.cl'],
    2:['19239843-1', 'camila', 'vargas salazar', '932387645', '966476663', 'camila.vs@correo.cl'],
}

mascotas = {
    # sexo, edad (meses), nombre, num_chip, raza, dueño_1,
    0:[0, 54, 'blanca', 120030, 0, 0],
    1:[1, 24, 'negro', 100293, 1, 2],
    2:[0, 75, 'homero', None, 2, 1],
}

razas = {
    # nombre_raza, especie
    0:['pastor aleman', 'perro'],
    1:['angora', 'gato'],
    2:['loro gris africano', 'loro']
}

veterinarios = {
    # rut, credencial, nombre, apellidos, fono, email
}

fichas_clinicas = {
    
}