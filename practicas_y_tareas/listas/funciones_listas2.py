def hay_multiplo_de_5(lista:list)->bool:
    i = 0
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i] % 5 == 0:
            encontrado = True
        i += 1
    return encontrado

def buscar_numero(lista:list,valor:int)->bool:
    i = 0
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i] == valor:
            encontrado = True
        i += 1
    return encontrado

def contiene_negativo(lista:list)->bool:
    i = 0
    encontrado = False
    while i < len(lista) and encontrado == False:
        if lista[i] < 0:
            encontrado = True
        i += 1
    return encontrado

def contar_mayores(numero:int,lista:list)->int:
    i = 0
    contador = 0
    while i < len(lista):
        if lista[i] > numero:
            contador += 1
        i += 1
    return contador
