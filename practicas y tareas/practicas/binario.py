def caracter_hexa(num):
    match num:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"
        case _: 
            return str(num)
        
numero = int(input("ingrese un numero: "))
hexa = ""
resultado = numero // 16
resto = numero % 16
hexa += caracter_hexa(resto)
numero = resultado
while resultado > 15:
    resultado = numero // 16
    resto = numero % 16
    hexa += caracter_hexa(resto)
    numero = resultado
hexa += str(resultado)
hexa2 = hexa[::-1]
print(hexa2)
        
        






'''
resultado = numero // 2
resto = numero % 2 
binario += str(resto)
numero = resultado
while resultado > 1:
    resultado = numero // 2
    resto = numero % 2 
    binario += str(resto)
    numero = resultado

binario += str(resultado)
binario2 = binario[::-1]
print(binario2)

if resultado > 1:
    numero = resultado
    resultado = numero // 2
    resto = numero % 2 
    binario += str(resto)
    if resultado > 1:
        numero = resultado
        resultado = numero // 2
        resto = numero % 2 
        binario += str(resto)
        if resultado > 1:
            numero = resultado
            resultado = numero // 2
            resto = numero % 2 
            binario += str(resto)
            if resultado > 1:
                numero = resultado
                resultado = numero // 2
                resto = numero % 2 
                binario += str(resto)
'''

