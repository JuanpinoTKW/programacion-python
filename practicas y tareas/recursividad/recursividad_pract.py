'''
def factorial(num:int)->int:
    if num == 0:
        resultado = 1
    else:  
        resultado = num * factorial(num - 1)

    return resultado

entero = int(input("ingrese un numero: "))
resultado = factorial(entero)
print(f"el factorial de {entero} es: {resultado}")

def digitos(num:int)->int:
    if num // 10 == 0:
        largo = 1
    else:  
        #num = num//10
        largo = 1 + digitos(num//10)
    return largo


def invertir(num:int)->int:
    if digitos(num) == 1:
        resultado = num 
    else:   
        resultado = num % 10 * 10 invertir(num)
    return resultado

entero = int(input("ingrese un numero: "))
resultado = invertir(entero)
print(f"el numero invertido de {entero} es: {resultado}")
'''