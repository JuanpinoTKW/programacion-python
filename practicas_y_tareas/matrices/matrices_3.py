"""
#3 Dada una matriz de MxN, escribí un programa que devuelva su transpuesta (intercambiar filas por columnas).
"""
import funciones_matrices
matriz_a = [
    [0,0,0],
    [0,0,0]
]
funciones_matrices.completar_matriz_ent(matriz_a)
for j in range(len(matriz_a[1])):
    for i in range(len(matriz_a)):
        print(matriz_a[i][j],end=" ")
        #print()
    print()