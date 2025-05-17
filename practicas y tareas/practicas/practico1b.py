#1 
nombre_de_usuario = input("ingrese su nombre ")
print("hola",nombre_de_usuario)

#2
numero = int(input("ingrese un numero "))
otro_numero = int(input("ingrese otro numero "))
print(numero+otro_numero)

#3
nombre = input("ingrese su nombre ")
edad = int(input("ahora ingrese su edad "))
apellido = input("y por ultimo ingrese su apellido ")
print("hola señor/a",nombre,apellido,"de",edad,"años")

#4
nombre = input("como se llama? ")
comision = int(input("ingrese su numero de comision "))
docente = input("cual es su docente? ")
asistencia = input("usted estuvo presente? ")
print("nombre:",nombre,"comision",comision,"docente:",docente,"asistio?:",asistencia)

#5
lado = int(input("ingrese un lado:"))
print("la superficie de un cuadrado es:",lado*lado,"cm cuadrados")

#6
largo = int(input("ingrese un largo: "))
ancho = int(input("ahora ingrese un ancho: "))
print("la superficie de un rectangulo es:",largo*ancho)

#7
base = int(input("ingrese el valor de la base: "))
altura = int(input("ahora ingrese la altura: "))
print("la superficie de un triangulo es de",base*altura/2,"cm")

#9
nombre = input("cual es su nombre? ")
apellido = input("cual es su apellido? ")
nota1 = int(input("ingrese su primer nota "))
nota2 = int(input("ingrese su 2da nota "))
nota3 = int(input("e ingrese su ultima nota "))
print("alumno:",nombre,apellido,"y su promedio es:",(nota1+nota2+nota3)/3)

#8
producto = input("ingrese un producto: ")
precio= int(input("cual es el precio?: "))
print("el iva del producto",producto,"es de",(precio*21)/100)

#10
name = input("ingrese su nombre ")
age = int(input("y ahora ingrese su edad "))
print("su edad dentro de 10 años sera:" + str(age+10) + "años.")
