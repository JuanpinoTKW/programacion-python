
'''
def pedir_numero_entero():
    numero = int(input("ingrese un numero: "))
    return numero


num = pedir_numero_entero()
print(num)


def pedir_numero_float():
    numero = float(input("ingrese un numero: "))
    return numero

num = pedir_numero_float()
print(num)

def pedir_cadena():
    cadena = input("ingrese una cadena ")
    return cadena

cad = pedir_cadena()
print(cad)

def calcular_area(base:int,altura:int):
    area = base * altura
    return area 

base = int(input("ingrese el valor de la base: "))
altura = int(input("ingrese el valor de la altura: "))
area = calcular_area(base,altura)    
print(area)
'''
def calcular_area(radio:float):
    pi = 3.14
    area = pi * radio ** 2
    return area 

radio = float(input("ingrese el valor de la radio: "))
area = calcular_area(radio)    
print(area)