# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

def pedir_num(base,exponente):
    num = int(input("ingrese la base de un numero: "))
    return num 

def pedir_potencia():
    potencia = int(input("ingrese el numero que desea elevar: "))
    return potencia

num = pedir_num
potencia = pedir_potencia
resultado = num ** potencia
print(f"el resultado es: {resultado}")

