"""
Dada una matriz cuadrada, escribí un programa que verifique si es simétrica respecto a su diagonal principal. 
(recordá que una matriz es simétrica si es igual a su transpuesta).
"""
import funciones_matrices
matriz_a = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
matriz_trasp = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
funciones_matrices.completar_matriz_ent(matriz_a)

for j in range(len(matriz_a[1])):
    for i in range(len(matriz_a)):
        matriz_trasp[i][j]=matriz_a[j][i]

funciones_matrices.imprimir_matriz(matriz_trasp)

if matriz_a == matriz_trasp:
    print(f"la matriz ingresada es simetrica respecto a su diagonal principal")
else:
    print("la matriz ingresada no es simetrica")