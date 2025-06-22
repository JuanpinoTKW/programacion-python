"""
En una empresa de desarrollo de software se gestionan 20 proyectos en simultáneo. Cada
proyecto tiene asignada una cantidad de días estimados para su finalización. A medida que
avanza el trabajo, el administrador puede agregar o restar días según el progreso o los
retrasos del proyecto.
Funcionalidades del programa
El sistema debe presentar un menú con las siguientes opciones:
1. Asignar días restantes a un proyecto
● El usuario ingresa el número de proyecto (entre 1 y 20).
● Luego indica la cantidad de días restantes para su finalización.
● No se permiten valores negativos ni 0 al ingresar la cantidad de días.
2. Ver los días restantes de un proyecto
● El usuario ingresa el número de proyecto (entre 1 y 20).
● El programa muestra la cantidad de días restantes de ese proyecto.
3. Modificar días restantes de un proyecto (Agregar o Restar)
● El usuario ingresa el número de proyecto (entre 1 y 20).
● El programa solicita si desea agregar o restar días.
● Si elige agregar o restar , debe ingresar una cantidad de días positiva mayor a 0.
● Al restar, se debe validar que el total de días restantes no quede negativo.
4. Buscar el proyecto con menos días restantes
● El programa recorre los 20 proyectos y muestra el número del proyecto que tenga
menos días restantes para su finalización.
● Se asume que solo existe un proyecto con la menor cantidad de días.
5. Mostrar todos los proyectos con los días restantes
● El programa debe mostrar la lista completa de los proyectos, indicando para cada
uno la cantidad de días restantes.
6. Salir del programa
Requisitos del desarrollo
● Se deben aplicar buenas prácticas de programación: el programa debe estar
modularizado con funciones claras y bien nombradas.
● No se permite el uso de funciones integradas como max(), min(), append(), etc, ni
ningún otro método directo de listas.
● Validar correctamente los datos ingresados:
○ El número de proyecto debe estar entre 1 y 20.
○ La cantidad de días debe ser mayor a 0.
○ Al restar días, no se debe permitir que el total de días restantes quede
negativo
"""
import validaciones_parcial

def inicializar_matriz(cant_filas:int)->list:
    matriz = []
    for i in range(cant_filas):
        filas = [i+1,0]
        matriz += [filas]
    return matriz

def asignar_dias(proyectos:list):
    proyecto = 1
    while proyecto > 0:
        proyecto = validaciones_parcial.validar_num_proyecto("[*]ingrese un proyecto (1-20) (0 para salir): ")
        if proyecto != 0:
            dias = validaciones_parcial.validar_dias("[*]ingrese los dias restantes para ese proyecto: ")
            for i in range(len(proyectos)):
                if proyectos[i][0] == proyecto:
                    proyectos[i][1] = dias
    print("")

def dias_restantes(proyectos:list):
    proyecto = validaciones_parcial.validar_num_proyecto("ingrese un proyecto (1-20): ")
    if proyecto > 0:
        for i in range(len(proyectos)):
            if proyectos[i][0] == proyecto:
                dias = proyectos[i][1] 
        print(f"[*]El proyecto {proyecto} tiene {dias} dias restantes")
    else:
        print("[*]ingrese un proyecto entre 1-20")
    print("")

def modificar_dias_restantes(proyectos:list):
    proyecto = validaciones_parcial.validar_num_proyecto("[*]ingrese un proyecto (1-20): ")
    if proyecto > 0:
        suma_o_resta = validaciones_parcial.validar_resta_suma("[*]desea restar o sumar días?: ")
        dias = validaciones_parcial.validar_dias("[*]ingrese la cantidad de dias: ")
        match suma_o_resta:
            case "sumar": 
                for i in range(len(proyectos)):
                    if proyectos[i][0] == proyecto:
                        proyectos[i][1] += dias
            case "restar":
                for i in range(len(proyectos)):
                    if proyectos[i][0] == proyecto:
                        if proyectos[i][1] >= dias:
                            proyectos[i][1] -= dias
                        else:
                            print(f"el proyecto {proyecto} tiene {proyectos[i][1]} días, no puede restar {dias}")
    else:
        print("[*]ingrese un proyecto entre 1-20")
    print("")

def proyecto_menor(proyectos:list):
    menos_dias = float('inf')
    proyecto_menor = 0
    for i in range(len(proyectos)):
        if proyectos[i][1] < menos_dias and proyectos[i][1] > 0:
            menos_dias = proyectos[i][1]
            proyecto_menor = proyectos[i][0]
    print(f"[*]el proyecto con la menor cantidad de dias es {proyecto_menor} que tiene {menos_dias} días")
    print("")

def mostrar_dias_restantes(proyectos:list):
    for i in range(len(proyectos)):
        print(f"[*]proyecto: {proyectos[i][0]}, dias restantes: {proyectos[i][1]}")
    print("")

proyectos = inicializar_matriz(20)
opcion = 0
while opcion != 6:
    print("1-Asignar dias restantes a un proyecto")
    print("2-Ver los días restantes de un proyecto")
    print("3-Modificar días restantes de un proyecto (Restar o Sumar)")
    print("4-Buscar el proyecto con menos dias restantes")
    print("5-Mostrar todos los proyectos con los días restantes")
    print("6-Salir del programa")
    opcion = int(input("ingrese la opcion deseada: "))
    match opcion:
        case 1: 
            asignar_dias(proyectos)
        case 2: 
            dias_restantes(proyectos)
        case 3: 
            modificar_dias_restantes(proyectos)
        case 4: 
            proyecto_menor(proyectos)
        case 5: 
            mostrar_dias_restantes(proyectos)
        case 6: 
            print("[*]saliendo")
        case _:
            print("[*]debe ingresar un numero entre 1-6")