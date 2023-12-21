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

## Sprint 2 (Módulo Registro y Seguimiento de Atenciones):

- [ ] Como Veterinario, necesito revisar las atenciones pasadas de una mascota para dar seguimiento del progreso de una mascota.

  - [ ] Crear la interfaz que tenga la lista de atenciones de una mascota en específico (Tiempo: 3 Horas)
  - [ ] Conectar con la base de datos y traer los datos de las atenciones (Tiempo: 2.6 Horas)

  **Total: 5.6 Horas**

- [ ] Como Veterinario, necesito mantener un registro detallado de la consulta para mantener un seguimiento detallado de cada caso.

  - [ ] Crear el front-end que tenga la lista de atenciones de un cliente en específico (Tiempo: 3.5 Horas)
  - [ ] Agregar un filtro al front-end para buscar una atención en específico (Tiempo: 3 Horas)
  - [ ] Crear el front-end de los detalles de la atención (Tiempo: 4 Horas)

  **Total: 10.5 Horas**

- [ ] Como Asistente, necesito modificar las horas de atención para corregir errores de digitación u cambios posteriores al registro en el sistema.

  - [ ] Crear la interfaz que visualice las horas de atención agendadas junto con el veterinario y una opción para cambiar la hora (Tiempo: 3.6 Horas)
  - [ ] Conectar con la base de datos para traer las horas específicas de una mascota (Tiempo: 2 Horas)
  - [ ] Guardar los cambios de la hora de atención modificada en la base de datos (Tiempo: 1 Hora)

  **Total: 6.6 Horas**

- [ ] Como Administrador, necesito crear perfiles dentro del sistema para poder dar distintos tipos de accesos al sistema.

  - [ ] Crear la interfaz en el que se visualice el formulario de administrador para agregar un nuevo perfil (Tiempo: 3 Horas)
  - [ ] Crear la lógica para generar una contraseña temporal segura (Tiempo: 2 Horas)
  - [ ] Conectar con la base de datos para almacenar el nuevo perfil (Tiempo: 1 Hora)
  - [ ] Crear la lógica para enviar la contraseña temporal por correo (Tiempo: 5 Horas)
  - [ ] Realizar las validaciones de los datos ingresados en el formulario (Tiempo: 3 Horas)

  **Total: 14 Horas**

- [ ] Como Administrador, necesito restablecer contraseñas de cuentas dentro del sistema para poder dar acceso nuevamente a una cuenta en caso de pérdida u error de acceso.

  - [ ] Crear la interfaz de usuario del módulo de administrador (Tiempo: 3 Horas)
  - [ ] Conectar con la base de datos para traer los datos del perfil del usuario (Tiempo: 2 Horas)
  - [ ] Crear la lógica para cambiar la contraseña a una temporal segura (Tiempo: 3 Horas)
  - [ ] Guardar los cambios en la base de datos (Tiempo: 1 Hora)

  **Total: 9 Horas**

#### Total del Sprint: 46.3 Horas

## Sprint 3 (Módulo de Agendamiento de Horas):

- [ ] Como Asistente, necesito agendar una hora de atención del cliente para poder reservar la hora de un veterinario.

  - [ ] Crear una interfaz que muestre el formulario (Tiempo: 3.3 Horas)
  - [ ] Validar cliente y veterinario (Tiempo: 2.7 Horas)
  - [ ] Validación de disponibilidad de horario (Tiempo: 4 Horas)
  - [ ] Ingreso de hora en la base de datos (Tiempo: 3.5 Horas)

  **Total: 13.5 Horas**

- [ ] Como Asistente, necesito visualizar todas las horas de los distintos veterinarios para poder agendar una hora libre y ver disponibilidad de los veterinarios.

  - [ ] Crear la interfaz que muestre el calendario con los bloques de hora, si esta está disponible, junto al veterinario y el botón para agendar hora con un cliente en específico (Tiempo: 9 Horas)
  - [ ] Conectar con la base de datos y traer los datos de las horas de los veterinarios (Tiempo: 2.5 Horas)

  **Total: 11.5 Horas**

- [ ] Como Asistente, necesito eliminar una hora de atención del cliente para eliminar una hora que ha sido cancelada y liberar la hora.

  - [ ] Crear una interfaz que muestre las horas de atención de un cliente (Tiempo: 3 Horas)
  - [ ] Conectar con la base de datos y traer las horas de atención de un cliente en específico (Tiempo: 2.5 Horas)
  - [ ] Realizar el cambio para eliminar la hora de atención de la base de datos (Tiempo: 2 Horas)

  **Total: 7.5 Horas**

- [ ] Como Asistente, necesito poder agendar horas sin la realización de una ficha clínica para atender mascotas rescatadas que no estén asociadas a un dueño.

  - [ ] Crear una interfaz que muestre el formulario (Tiempo: 3 Horas)
  - [ ] Validar cliente como NN y veterinario disponibilidad de horario (Tiempo: 3 Horas)
  - [ ] Ingreso de hora en la base de datos (Tiempo: 1 Hora)

  **Total: 7 Horas**

- [ ] Como Asistente, necesito visualizar el veterinario a cargo de una mascota para poder ver disponibilidad y agendar una hora con este veterinario.

  - [ ] Crear la interfaz que visualice un veterinario en específico junto a sus datos y horas disponibles (Tiempo: 4 Horas)
  - [ ] Conectar con la base de datos para traer un veterinario especifico junto con sus horas disponibles (Tiempo: 4 Horas)

  **Total: 8 Horas**

#### Total del Sprint: 47.5 Horas
