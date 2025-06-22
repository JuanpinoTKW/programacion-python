"""
Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). 
La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ejemplo, si la cadena ingresada es “murcielaguito”, la salada por pantalla deberá ser: (“a”: 1; “e”: 1; “i”: 2; “o”: 1; “u”:2)
"""
cadena = "me gusta jugar a los videojuegos"
matriz = [
    ["a",0],
    ["e",0],
    ["i",0],
    ["o",0],
    ["u",0]
]

for caracter in cadena:
    if caracter == 'a':
        matriz[0][1] += 1
    if caracter == 'e':
        matriz[1][1] += 1
    if caracter == 'i':
        matriz[2][1] += 1
    if caracter == 'o':
        matriz[3][1] += 1
    if caracter == 'u':
        matriz[4][1] += 1

#print(f"la letra 'a' aparece {cont_a} veces; la letra 'e' aparece {cont_e} veces; la letra 'i' aparece {cont_i}, la letra 'o' aparece {cont_o}; y la letra 'u' aparece {cont_u}")
print(matriz)