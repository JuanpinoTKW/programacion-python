'''
Realiza un programa que permita al usuario ingresar un número entero positivo. '
El programa debe mostrar en pantalla todos los números enteros desde 1 hasta ese número, saltando los números pares '
'(es decir, solo debe mostrar los impares).'
'''
num = int(input("ingrese un numero entero positivo: "))
for num in range (1 , num , 2):
    print(num)
if num <= 1:
    print("se produjo un error")

