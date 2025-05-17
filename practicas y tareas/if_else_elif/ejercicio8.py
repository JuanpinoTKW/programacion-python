'''
Ejercicio 2 
Escribir un programa que pregunte el nombre del usuario en la consola(usando input) y 
después de que el usuario lo introduzca muestre por pantalla la cadena ”<nombre>”, 
donde <nombre> es el nombre que el usuario haya introducido.

#nombre = input("ingrese su nombre ")
#print("hola",nombre)

#7
Tenemos que obtener el sueldo (por input) que el usuario nos ingrese , transformarlo en 
número entero y mostrar el importe de sueldo actualizado con el incremento del 15% 
utilizando print.

sueldo = int(input("ingrese su sueldo= "))
print("su inporte es: ",(sueldo*1.15))

Ejercicio 8
Tenemos que obtener los valores (por input) que el usuario nos ingrese (sueldo e incremento),
transformarlos en números enteros y mostrar el importe de sueldo actualizado con el
incremento porcentual utilizando print.

sueldo = int(input("ingrese su sueldo: "))
incremento = int(input("e ingrese el incremento: "))
sueldo_incrementado = (sueldo * incremento / 100)+sueldo
print(f"su sueldo es: {sueldo}, el incremento es: {incremento} y su sueldo incrementado es: {sueldo_incrementado}")

Ejercicio 9
Tenemos que crear un programa que deberá obtener el importe que ingrese el usuario por
consola(input), transformar en número y mostrar el importe actualizado con un descuento
del 20% utilizando print.

importe = int(input("ingrese un importe: "))
descuento = (importe*20)/100
importe_descuento = importe-descuento
print(f"su importe actualizado es {importe_descuento}")

Ejercicio 10
Tenemos que crear un programa que deberán obtener el importe y el descuento que ingrese el
usuario por consola, transformarlos en números y mostrar el importe actualizado con el
descuento utilizando print.

importe = float(input("ingrese un importe: "))
porcentaje = float(input("ingrese el descuento: "))
descuento = (importe*porcentaje)/100
importe_descuento = importe-descuento
print(f"su importe actualizado es {importe_descuento} el descuento es {descuento}")

Agencia de viaje:
Para saber el costo de un viaje necesitamos el siguiente algoritmo, sabiendo que el precio por
kilo de pasajero es 1000 pesos.Se ingresan todos los datos por INPUT los datos a solicitar de
dos personas son: nombre, edad y peso
Se pide armar el siguiente mensaje:
"Hola jose y maria , sus pesos son 80 kilos y 60 kilos respectivamente, sumados da 140 kilos ,
el promedio de edad es 33 y su viaje vale 140000 pesos "

precio_kilo = 1000
nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
peso = int(input("ingrese su peso: "))
nombre2 = input("ingrese su nombre: ")
edad2 = int(input("ingrese su edad: "))
peso2 = int(input("ingrese su peso: "))
promedio_edad = (edad+edad2)/2
pesos = peso + peso2
valor_viaje = pesos*precio_kilo
#print(f"hola {nombre} y {nombre2},sus pesos son {peso} kilos y {peso2} respectivamente, sumados da {pesos} kilos, el promedio de edad es {promedio_edad} y su viaje vale {valor_viaje}")
print("hola " + nombre + " y " + nombre2 + " sus pesos son " + str(peso) + " kilos y " + str(peso2) + " respectivamente, sumados da " + str(pesos) + " kilos, el promedio de edad es " + str(promedio_edad) + " y su viaje vale " + str(valor_viaje))

Ejercicio 8
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá
determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
● Menos de 160 cm: Base
● Entre 160 cm y 179 cm: Escolta
● Entre 180 cm y 199 cm: Alero
● 200 cm o más: Ala-Pívot o Pívot
'''
altura = int(input("ingrese su altura: "))
if altura < 160:
    print("su posicion es base")
if altura >= 160 and altura <= 179:
    print("su posicion es escolta")
if altura >= 180 and altura <= 199:
    print("su posicion es alero")
elif altura >= 200:
    print("su posicion es ala-pivot o pivot")
