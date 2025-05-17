'''
Empresa de Camiones:
Para el departamento de logística:
A. Es necesario saber la cantidad de camiones que harían falta para transportar los
materiales que se utilizarán para la construcción de un edificio. Para ello, se ingresa la
cantidad de toneladas necesarias de materiales a transportar. El programa deberá
informar la cantidad de camiones, sabiendo que cada uno de ellos puede transportar por
viaje 3500kg.
B. A partir del ingreso de la cantidad de kilómetros que tiene que recorrer estos camiones
para llegar al destino de la obra, necesitamos que el programa informe cual es el tiempo
(en horas) que tardará cada uno de los camiones, si sabemos que cada camión puede ir
a una velocidad máxima y constante de 90 km/h.

kilos = int(input("ingrese la cantidad de kilos: "))
km = int(input("ingrese la distancia (en km): "))
cantidad_camiones = kilos / 3500
horas = km / 90
print(f"los camiones a transportar son {cantidad_camiones}, y el tiempo en hacer el trayecto es {horas} horas")

Ejercicio 10
Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. Determinar si el
empleado debe o no pagar el impuesto a las ganancias. El mismo no se pagará si el empleado es
casado con hijos y sus ingresos son menores a $2200000.

sueldo = int(input("ingrese su suelo: "))
estado_civil = input("su estado civil es casado o soltero?: ")
cantidad_hijos = int(input("ingrese la cantidad de hijos que tiene: "))
if sueldo < 2200000 and cantidad_hijos > 0 and estado_civil == "casado":
    print("no pagará impuesto a las ganancias.")
else:
    print("pagará impuesto a las ganancias")

Ejercicio 9
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde
los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado
(si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en
base a la información suministrada.
'''
naturalizado_o_nativo = input("usted es naturalizado o nativo?: ")
edad = int(input("ingrese su edad: "))
if naturalizado_o_nativo == "nativo" and edad >= 16:
    print("usted puede votar (por opción)")
elif naturalizado_o_nativo == "naturalizado" and edad >= 18:
    print("usted puede votar (obligatoriamente)")
else:
    print("usted no puede")


