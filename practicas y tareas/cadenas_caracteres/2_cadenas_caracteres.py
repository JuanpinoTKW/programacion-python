#2 Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera ocurrencia 
# de dicho caracter, o -1 en caso de que no esté.
import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def devolver_indice(cadena:str,caracter:str)->int:
    cont = 0
    encontrado = False
    for letra in cadena:
        if letra == caracter and encontrado == False:
            encontrado = True
            posicion = cont
        cont += 1
    
    if encontrado == True:
        return posicion
    else:
        return -1

        
cadena = validaciones.validar_texto("ingrese un texto: ")
caracter_a_buscar = input("ingrese la letra a buscar en ese texto: ")
indice = devolver_indice(cadena,caracter_a_buscar)
print(indice)