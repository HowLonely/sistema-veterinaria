# Sistema Veterinaria

## Sprint 1 (Módulo Ficha Clínica):

- [ ] Como Asistente, necesito registrar los datos de una mascota en una ficha clínica junto a su dueño para mantener un registro ordenado y tener acceso posteriormente a la información relacionada.

Tiempo(Esfuerzo): 4+2+1 = 7 Horas

- [ ] Como Asistente, necesito mantener registros de los dueños junto a sus mascotas para facilitar el acceso a la información al realizar operaciones específicas.

Tiempo(Esfuerzo): 8+3.5+1.5 = 13 Horas

- [ ] Como Veterinario, necesito tener acceso a los datos detallados de una mascota para tener más contexto al realizar el diagnóstico.

Tiempo(Esfuerzo): 3+2+2+4 = 11 Horas

- [ ] Como Asistente, necesito hacer CRUD a los datos de los dueños de una o más mascotas para mantener actualizado el sistema con respecto a los dueños de las mascotas.

Tiempo(Esfuerzo): 2.6+4+3+1 = 10.6 Horas

- [ ] Como Asistente, necesito hacer CRUD a todas las razas disponibles en el sistema para poder asociarlas a la mascota.

Tiempo(Esfuerzo): 3+2+5+1+1 = 12 Horas

#### Total: 53.6 Horas

Sprint 2 - Módulo de Registro y Seguimiento de Atenciones (45.7 Horas: 24/11 – 8/12):

•	Como Veterinario, necesito revisar las atenciones pasadas de una mascota para dar seguimiento del progreso de una mascota.
1.	Crear la interfaz que tenga la lista de atenciones de una mascota en específico (3 Horas)
2.	Conectar con la base de datos y traer los datos de las atenciones (2.6 Horas)
	Tiempo Total: 5.6 Horas

•	Como Veterinario, necesito mantener un registro detallado de la consulta para mantener un seguimiento detallado de cada caso.
1.	Crear el front-end que tenga la lista de atenciones de un cliente en específico (3.5 Horas)
2.	Agregar un filtro al front-end para buscar una atención en específico (3 Horas)
3.	Crear el front-end de los detalles de la atención (4 Horas)
	Tiempo Total: 10.5 Horas

•	Como Asistente, necesito modificar las horas de atención para corregir errores de digitación u cambios posteriores al registro en el sistema.
1.	Crear la interfaz que visualice las horas de atención agendadas junto con el veterinario y una opción para cambiar la hora (3.6 Horas)
2.	Conectar con la base de datos para traer las horas específicas de una mascota (2 Horas)
3.	Guardar los cambios de la hora de atención modificada en la base de datos (1 Hora)
	Tiempo Total: 6.6 Horas

•	Como Administrador, necesito crear perfiles dentro del sistema para poder dar distintos tipos de accesos al sistema.
1.	Crear la interfaz en el que se visualice el formulario de administrador para agregar un nuevo perfil (3 Horas)
2.	Crear la lógica para generar una contraseña temporal segura (2 Horas)
3.	Conectar con la base de datos para almacenar el nuevo perfil (1 Hora)
4.	Crear la lógica para enviar la contraseña temporal por correo (5 Horas)
5.	Realizar las validaciones de los datos ingresados en el formulario (3 Horas)
	Tiempo Total: 14 Horas

•	Como Administrador, necesito restablecer contraseñas de cuentas dentro del sistema para poder dar acceso nuevamente a una cuenta en caso de pérdida u error de acceso.
1.	Crear la interfaz de usuario del módulo de administrador (3 Horas)
2.	Conectar con la base de datos para traer los datos del perfil del usuario (2 Horas)
3.	Crear la lógica para cambiar la contraseña a una temporal segura (3 Horas)
4.	Guardar los cambios en la base de datos (1 Hora)
	Tiempo Total: 9 Horas

Sprint 3 - Módulo de Agendamiento de Horas (47.5 Horas: 8/12 – 22/12):

•	Como Asistente, necesito agendar una hora de atención del cliente para poder reservar la hora de un veterinario.
1.	Crear una interfaz que muestre el formulario (3.3 Horas)
2.	Validar cliente y veterinario (2.7 Horas)
3.	Validación de disponibilidad de horario (4 Horas)
4.	Ingreso de hora en la base de datos (3.5 Horas)
	Tiempo Total: 13.5 Horas

•	Como Asistente, necesito visualizar todas las horas de los distintos veterinarios para poder agendar una hora libre y ver disponibilidad de los veterinarios.
1.	Crear la interfaz que muestre el calendario con los bloques de hora, si esta está disponible, junto al veterinario y el botón para agendar hora con un cliente en específico (9 Horas)
2.	Conectar con la base de datos y traer los datos de las horas de los veterinarios (2.5 Horas)
	Tiempo Total: 11.5 Horas

•	Como Asistente, necesito eliminar una hora de atención del cliente para eliminar una hora que ha sido cancelada y liberar la hora.
1.	Crear una interfaz que muestre las horas de atención de un cliente (3 Horas)
2.	Conectar con la base de datos y traer las horas de atención de un cliente en específico (2.5 Horas)
3.	Realizar el cambio para eliminar la hora de atención de la base de datos (2 Horas)
	Tiempo Total: 7.5 Horas

•	Como Asistente, necesito poder agendar horas sin la realización de una ficha clínica para atender mascotas rescatadas que no estén asociadas a un dueño.
1.	Crear una interfaz que muestre el formulario (3 Horas)
2.	Validar cliente como NN y veterinario disponibilidad de horario (3 Horas)
3.	Ingreso de hora en la base de datos (1 Hora)
	Tiempo Total: 7 Horas

•	Como Asistente, necesito visualizar el veterinario a cargo de una mascota para poder ver disponibilidad y agendar una hora con este veterinario.
1.	Crear la interfaz que visualice un veterinario en específico junto a sus datos y horas disponibles (4 Horas)
2.	Conectar con la base de datos para traer un veterinario especifico junto con sus horas disponibles (4 Horas)
	Tiempo Total: 8 Horas
