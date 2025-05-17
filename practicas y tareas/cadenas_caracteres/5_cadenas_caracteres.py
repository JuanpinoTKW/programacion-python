#Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.

#Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.


import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def suprimir_vocales(cadena:str)->str:
    palabra_resultado = ""
    for caracter in cadena:
        if caracter.upper() != "A" and caracter.upper() != "E" and caracter.upper() != "I" and caracter.upper() != "O" and caracter.upper() != "U":
            palabra_resultado += caracter
        ultimo_caracter = caracter
    return palabra_resultado

palabra = validaciones.validar_texto("ingrese una palabra: ")
#texto = eliminar_repetidos(palabra)
print(suprimir_vocales(palabra))