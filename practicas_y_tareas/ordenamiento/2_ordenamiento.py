#Crear una función intercalar_vectores que reciba dos vectores de números enteros ordenados en orden ascendente, 
#y devuelva un único vector también ordenado. La función debe tener un parámetro opcional descendente para que el vector resultante esté en 
#orden descendente.

def intercalar_vectores(vector1:list,vector2:list,descendente=False)->list:
    vector_resultado = [0] * (len(vector1) + len(vector2))
    v1 = 0
    v2 = 0
    for i in range(len(vector_resultado)):
        if vector1[v1] < vector2[v2]:
            valor = vector1[v1]
            if v1 < len(vector1)-1:
                v1 += 1
        else:
            valor = vector2[v2]
            if v2 < len(vector2)-1:
                v2 += 1
        vector_resultado[i] = valor
    return vector_resultado

vector1 = [2,4,6,8,11]
vector2 = [1,3,5,7,9]
print(intercalar_vectores(vector1,vector2))