"""
Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.


num = 1

def determinar_par_o_impar(numero:int):
    resto = numero % 2
    if resto == 0:
        print("el numero ingresado es par")
    else:
        print("el numero ingresado es impar")

while num != 0:
    num = int(input("ingrese un numero: "))
    if num != 0:
        determinar_par_o_impar(num)


def determinar_par(numero:int)->bool:
    resto = numero % 2
    if resto == 0:
        return True
    else:
        return False
    
num = 1

while num != 0:
    num = int(input("ingrese un numero: "))
    if num != 0:
        #print(determinar_par(num))
        #es_par = determinar_par(num)
        #print(es_par)
        if determinar_par(num) == True:
            print("es par.")
        else:
            print("es impar.")

def el_mayor(numero1:int,numero2:int,numero3:int)->int:
    if numero1 > numero2:
        if numero1 > numero3:
            return numero1
        else: 
            return numero3
    else:
        if numero2 > numero3:
            return numero2
        else: 
            return numero3

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
num3 = int(input("ingrese un numero: "))

print(f"el numero mayor es: {el_mayor(num1,num2,num3)}")

def potencia(base:int,exponente:int)->int:
    potencia = base ** exponente
    return potencia

num = int(input("ingrese un numero entero positivo: "))
num2= int(input("ingrese un numero entero positivo: "))
print(f"la potencia es: {potencia(num,num2)}")

def es_primo(num:int)->bool:
    if num <= 1:
        return False
    for i in range(2,int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

num = int(input("ingrese un numero "))
if es_primo(num) == True:
    print(f"es primo.")
else:
    print(f"no es primo.")

import funciones
cont = 0

num = int(input("ingrese un numero entero: "))
for i in range(1 , num + 1):
    if funciones.es_primo(i) == True:
        cont += 1
    
print(f"la cantidad de numero primos entre 1 y {num} es de: {cont}")
"""

import funciones
num = int(input("imprimir tabla del: "))
iniciar = int(input("iniciar en: "))  
fin = int(input("finalizar en: "))

funciones.imprimir_tabla(num,iniciar,fin)
