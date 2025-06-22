#Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. 
#Deberá retornar un valor booleano indicando lo sucedido.
import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def es_palindromo(cadena:str)->bool:
    cadena_inv = ""
    for caracter in cadena[::-1]:
        cadena_inv += caracter
    
    if cadena == cadena_inv:
        es_o_no = True
    else:
        es_o_no = False

    return es_o_no

palabra = validaciones.validar_texto("ingrese una palabra: ")
#print(es_palindromo(palabra))
if es_palindromo(palabra) == True:
    print(f"La palabra {palabra} es palindromo")
else:
    print(f"La palabra {palabra} NO es palindromo")