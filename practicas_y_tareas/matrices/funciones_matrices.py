import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

def completar_matriz_ent(matriz:list)->list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = validaciones.validar_entero_pos(f"ingrese un numero en la posicion {[i]} y en la columna {[j]} ")
    return matriz

def imprimir_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=" ")
        print()
    print()
    return 

def completar_matriz_str(matriz:list)->list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input(f"ingrese un caracter en la posicion {[i]} y en la columna {[j]}")
        print()
    print()
    return matriz
