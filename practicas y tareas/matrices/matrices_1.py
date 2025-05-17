"""
#1 Dada una matriz de números enteros, escribí un programa que calcule la suma total de todos sus elementos.
"""
import funciones_matrices

matriz_a = [
    [0,0],
    [0,0]
]
matriz_b = [
    [0,0],
    [0,0]
]
matriz_resultado = [
    [0,0],
    [0,0]
]
funciones_matrices.completar_matriz_ent(matriz_a)
funciones_matrices.completar_matriz_ent(matriz_b)

for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        matriz_resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

funciones_matrices.imprimir_matriz(matriz_resultado)