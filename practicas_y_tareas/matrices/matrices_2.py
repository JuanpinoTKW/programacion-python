"""
Dada una matriz de números enteros, escribí un programa que encuentre y muestre el número más grande y el número más chico.
"""

import funciones_matrices

matriz_a = [
    [0,0],
    [0,0]
]

funciones_matrices.completar_matriz_ent(matriz_a)

valor_max = 0
valor_min = float('inf')
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        if matriz_a[i][j] > valor_max:
            valor_max = matriz_a[i][j]
        if matriz_a[i][j] < valor_min:
            valor_min = matriz_a[i][j]

print(f"el numero mas grande es {valor_max}, y el numero mas chico es {valor_min}")
