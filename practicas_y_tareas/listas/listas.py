from validaciones import validar_entero
from funciones_listas2 import *
"""
Crear una función buscar_numero(lista, valor) que reciba una lista y un número, y devuelva si el número se encuentra o no en la lista.
Probar la función cargando una lista de 5 números desde el teclado y solicitando un número a buscar.
    

lista = [0] * 5
for i in range(0,5):
    num = validar_entero("ingrese un numero: ")
    lista[i] = num
buscar = validar_entero("ingrese el numero a buscar: ")
if buscar_numero(lista,buscar) == True:
    print(f"el numero {buscar} ha sido encontrado")
else:
    print(f"no se ha encontrado el numero {buscar}")

 Crear una función hay_multiplo_de_5(lista) que reciba una lista de números y devuelva si hay al menos un múltiplo de 5 en la lista.
 Probar la función ingresando 6 números desde teclado.

lista = [0] * 6
for i in range(0,6):
    num = validar_entero("ingrese un numero: ")
    lista[i] = num

if hay_multiplo_de_5(lista) == True:
    print(f"hay un multiplo de 5")
else:
    print(f"no hay nigun multiplo de 5")


Crear una función contiene_negativo(lista) que reciba una lista de números enteros y devuelva si hay algún número negativo en la lista.
Solicitar al usuario 5 números para probar la función.

lista = [0] * 5
for i in range(0,5):
    num = int(input("ingrese un numero: "))
    lista[i] = num

if contiene_negativo(lista) == True:
    print(f"hay un numero negativo")
else:
    print(f"no hay nigun numero negativo")

Crear una función contar_mayores (número , lista) que reciba el número a buscar y una lista de números 
y devuelva cuántos números hay mayores al recibido.


lista = [0] * 5
for i in range(0,5):
    num = int(input("ingrese un numero: "))
    lista[i] = num


numero = int(input("ingrese el numero a buscar: "))
cantidad = contar_mayores(numero,lista)
print(f"la cantidad de numeros mayores a {numero} son {cantidad}")

Crear una función contiene_cero(lista) que reciba una lista de números enteros y devuelva si existe al menos un cero en la lista.
"""
def hay_cero(lista:list)->bool:
    i = 0
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i] == 0:
            encontrado = True
        i += 1
    return encontrado

lista = [0] * 6
for i in range(0,6):
    num = validar_entero("ingrese un numero: ")
    lista[i] = num

if hay_cero(lista) == True:
    print(f"hay un cero")
else:
    print(f"no hay nigun cero")