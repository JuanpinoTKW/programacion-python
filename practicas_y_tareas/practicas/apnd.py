"""
Enunciado
En una oficina de soporte técnico, los empleados trabajan por turnos de lunes a domingo. Cada día de la semana trabaja una sola persona distinta.

Se desea desarrollar un programa que utilice una lista de 7 posiciones (una por cada día, de lunes a domingo) y ofrezca al administrador un menú 
con las siguientes opciones:

Asignar empleados a los días de la semana: el usuario ingresa un número del 1 al 7 (donde 1 representa lunes y 7 domingo), y luego ingresa el 
nombre del empleado que trabajará ese día.
Buscar qué día trabajó cierto empleado: el usuario ingresa un nombre y el programa indica qué día de la semana trabajó (si está asignado).
Reemplazar el nombre de un empleado por otro: el usuario indica un nombre a buscar y el nuevo nombre que debe reemplazarlo.
Mostrar el nombre más largo entre los empleados asignados (es decir, el que tenga más letras).
Salir del programa.
"""
import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def asignar_empleado(empleados:list):
    nombre_emp = validaciones.validar_texto("ingrese el nombre del empleado: ")
    dia = validaciones.validar_dias("ingrese un dia del 1-7: ")
    empleados[dia-1] = nombre_emp

def buscar_dia(empleados:list):
    nombre_emp = validaciones.validar_texto("ingrese el nombre del empleado: ")
    for i in range(len(empleados)):
        if empleados[i] == nombre_emp:
            match i:
                case 0:
                    print(f"[*]el empleado {nombre_emp} trabajo el lunes")
                case 1:
                    print(f"[*]el empleado {nombre_emp} trabajo el martes")
                case 2:
                    print(f"[*]el empleado {nombre_emp} trabajo el miercoles")
                case 3:
                    print(f"[*]el empleado {nombre_emp} trabajo el jueves")
                case 4:
                    print(f"[*]el empleado {nombre_emp} trabajo el viernes")
                case 5:
                    print(f"[*]el empleado {nombre_emp} trabajo el sabado")
                case 6:
                    print(f"[*]el empleado {nombre_emp} trabajo el domingo")

def reemplazar_empleado(empleados:list):
    nombre_emp = validaciones.validar_texto("ingrese el nombre del empleado a reemplazar: ")
    emp_nuevo = validaciones.validar_texto("ingrese el nombre del nuevo empleado: ")
    for i in range(len(empleados)):
        if nombre_emp == empleados[i]:
            emp_nuevo = empleados[i]
            
def nombre_largo(empleados:list):
    nombre_mas_largo = ""
    largo = 0
    for i in range(len(empleados)):
        if len(empleados[i]) > largo:
            nombre_mas_largo = empleados[i]
            largo = len(empleados[i])
        
    print(f"[*]el empleado con el nombre mas largo es: {nombre_mas_largo}")


empleados = [""] * 7
opcion = 0
while opcion != 5:
    print("1-Asignar empleados a los dias de la semana")
    print("2-Buscar que dia trabajo cierto empleado")
    print("3-Reemplazar el nombre de un empleado por otro")
    print("4-Mostrar el nombre mas largo")
    print("5-Salir del programa")
    opcion = int(input("ingrese la opcion deseada: "))
    match opcion:
        case 1:
            asignar_empleado(empleados)
        case 2:
            buscar_dia(empleados)
        case 3:
            reemplazar_empleado(empleados)
        case 4:
            nombre_largo(empleados)
        case 5:
            print("saliendo")
        case _:
            print("opcion no disponible")
print(empleados)