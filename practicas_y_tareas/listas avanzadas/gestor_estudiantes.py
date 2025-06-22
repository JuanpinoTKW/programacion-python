"""
🗂️ Enunciado: Gestor de Estudiantes (ABM con listas paralelas)
La UTN está desarrollando un pequeño sistema para administrar estudiantes en su nueva Facultad Regional. Vas a trabajar con listas paralelas 
para almacenar los datos de cada estudiante.
Tenés tres listas:
nombres: almacena los nombres de los estudiantes.


edades: almacena sus edades (enteros).


legajos: almacena los números de legajo (enteros, únicos).


El programa debe mostrar un menú con las siguientes opciones:
Menú:
1. Alta de estudiante (cargar nuevo estudiante)
2. Baja de estudiante (eliminar por número de legajo)
3. Modificar datos de estudiante (nombre o edad, buscar por legajo)
4. Listar todos los estudiantes (ordenados por nombre)
5. Buscar estudiante por nombre (mostrar legajo y edad)
6. Clonar base de datos (shallow copy y deep copy)
7. Vaciar base de datos (clear)
8. Salir

💡Tené en cuenta que…

Todas las listas deben estar sincronizadas: el índice i representa al mismo estudiante en todas las listas.


Verificá que los legajos no se repitan al dar de alta.


Al borrar o modificar, buscá por número de legajo. Si no existe, mostrale un mensaje al usuario.


Permití al usuario ingresar datos por consola y repetí el menú hasta que elija salir.
"""
nombres = ["Javier","Juan","Marta","Sandra","Marcos","Milena"]
edades = [18,19,20,21,22,24]
legajos = [1001,1002,1003,1004,1005,1006]

opcion = 0
while opcion != 8:
    print("1. Alta de estudiante (cargar nuevo estudiante)")
    print("2. Baja de estudiante (eliminar por número de legajo)")
    print("3. Modificar datos de estudiante)")
    print("4. Listar todos los estudiantes")
    print("5. Buscar estudiante por nombre")
    print("6. Clonar base de datos")
    print("7. Vaciar base de datos")
    print("8. Salir")
    print("")
    opcion = int(input("ingrese la opcion deseada:"))
    match opcion:
        case 1:
            nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
            edad_nuevo_estudiante = int(input("ingrese su edad: "))
            legajo_nuevo_estudiante = int(input("ingrese su numero de legajo: "))
            if legajo_nuevo_estudiante > 1006:
                legajos.append(legajo_nuevo_estudiante)
            else:
                print("el numero debe ser mayor a '1006'")
            nombres.append(nuevo_estudiante)
            edades.append(edad_nuevo_estudiante)
            legajo_nuevo_estudiante = legajos.index(5,+1)
            print(legajo_nuevo_estudiante)
        case 2:
            eliminar = int(input("ingrese el estudiante que desee eliminar por numero de legajo: "))
            nombres.remove(eliminar)
        case 3:
            modificar_datos = int(input("ingrese el numero de legajo del estudiante: "))
            if modificar_datos < legajos and modificar_datos > legajos:
                nombre_o_edad = input("desea cambiar la edad o nombre?: ")
                match nombre_o_edad:
                    case "edad":
                        nueva_edad = int(input("ingrese la nueva edad: "))
                        
        case 4:
            print("")
        case 5:
            print("")
        case 6:
            print("")
        case 7:
            print("")
        case 8:
            print("saliendo del programa")
        case _:
            print("debe ingresar un numero entre 1-8")
