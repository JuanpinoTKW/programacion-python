# Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
'''
i = 0
suma = 0
salir = 0

while salir == 0:
    numero = int(input("ingrese un numero (ingrese 0 para salir): "))
    suma += numero
    i += 1
    if numero == 0:
        salir = 1

promedio = suma / i
print(f"la suma de los numeros ingresados es {suma}, y el promedio es {promedio}")
'''
# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.
cont = 1
suma = 0
continuar = "s"

while cont <= 10 and continuar == "s":
    numero = int(input("ingrese un numero: "))
    suma += numero
    cont += 1
    if cont > 5:
        continuar = input("desea ingresar otro numero? (s/n) ").lower()

promedio = suma / cont
print(f"la suma de los numeros ingresados es {suma} y el promedio es {promedio}")