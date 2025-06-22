#Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.


	#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def eliminar_repetidos(cadena:str)->str:
    ultimo_caracter = ""
    palabra_resultado = ""
    for caracter in cadena:
        if caracter != ultimo_caracter:
            palabra_resultado += caracter
        ultimo_caracter = caracter
    return palabra_resultado

palabra = validaciones.validar_texto("ingrese una palabra: ")
#texto = eliminar_repetidos(palabra)
print(eliminar_repetidos(palabra))