#Crear una función llamada ordenar_array que reciba como parámetro un array de números enteros y lo ordene de forma ascendente. 
#La función debe implementar como algoritmo de ordenamiento el método de la burbuja. Además, como parámetro opcional debe recibir un booleano 
#(que por default está en False), que en caso de ser True ordena el vector en forma descendente.

import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def ordenar_array(lista:list,descendente=False)->list:
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if descendente == False:
                if lista[j] > lista[j+1]:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp
            else:
                if lista[j] < lista[j+1]:
                    temp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = temp

    return lista

numeros = [5,2,9,6,3,8,1]
print(ordenar_array(numeros,True))