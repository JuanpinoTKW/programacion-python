'''
Una biblioteca universitaria desea realizar una encuesta para conocer mejor a sus usuarios. Se pide desarrollar un programa en Python que:
Solicite los datos de varias personas hasta que el usuario decida no continuar.
Valide cada dato correctamente.
Utilice funciones para validar los ingresos.

Al finalizar, muestre estadísticas simples.

Nombre (solo texto, no vacío y mayor a 2 caracteres).
Edad (entre 12 y 99 años inclusive).
Género: “Femenino”, “Masculino” o “Otro”.
Cantidad de libros leídos por mes (entero >= 0).
¿Es socio de la biblioteca? (“Sí” o “No”).

'''
personas = 0
libros_leidos = 0
si_socios = 0
no_socios = 0
lectores = 0
edades = 0
masculino = 0
femenino = 0
otro = 0
max_lec_nombre = ""
max_lec_cantidad = 0

import validaciones

pedir_datos = "S"
while pedir_datos == "S":
    usuario = validaciones.validar_texto("ingrese su usuario: ")
    edad = validaciones.validar_entero("ingrese su edad: ")
    genero = validaciones.validar_genero("ingrese su genero, m/f/x: ")
    libros = validaciones.validar_entero("cuantos libros leyo?: ")
    socio = validaciones.validar_sino("es socio? S/N: ")
    personas += 1
    libros_leidos += libros
    if socio == "S":
        si_socios += 1
    else:
        no_socios += 1
    if libros > 5:
        lectores += 1
        edades += edad
    match genero:
        case "M":
            masculino += 1
        case "F":
            femenino += 1
        case "X":
            otro += 1
    if libros > max_lec_cantidad:
        max_lec_cantidad = libros
        max_lec_nombre = usuario
    pedir_datos = validaciones.validar_sino("desea cargar mas datos? S/N?")

promedio_libros = libros_leidos / personas
promedio_edad_lectores = edades / lectores

print(f"el total de personas encuestadas es {personas}, el promedio de libros leidos es de {libros_leidos}, los socios son {si_socios} y los no socios {no_socios}. los hombres son {masculino}, mujeres {femenino} y otros {otro}; el mayor lector fue {max_lec_nombre} que leyo {max_lec_cantidad} libros")