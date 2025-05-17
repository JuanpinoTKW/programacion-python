#1. Desarrollar una función que permita crear un array de números con la cantidad de elementos que establezca el parámetro recibido.

def crear_array(elementos:int)->list:
    lista = [0] * elementos
    return lista

#2 Escribir una función que permita ingresar la cantidad de números que reciba como parámetro.  Crear el array con la función del punto 1.

def lista_nums(cant_num:int)->list:
    lista = crear_array(cant_num)
    for i in range(cant_num):
        lista[i] = int(input("ingrese un numero: "))
    return lista

#3 Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números. 

def lista_promedio(lista_entero:list)->int:
    acumulador = 0
    for i in range(len(lista_entero)):
        acumulador += lista_entero[i]
    promedio = acumulador / len(lista_entero)
    return promedio

#4 Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.

def lista_promedios_pos(lista_entero:list)->int:
    acumulador = 0
    contador = 0
    for i in range(len(lista_entero)):
        if lista_entero[i] > 0:
            acumulador += lista_entero[i]
            contador += 1
    promedio = acumulador / contador
    return promedio

#5 Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.

def lista_producto(lista_nums:list)->int:
    acumulador = lista_nums[0]
    i = 1
    while i <= len(lista_nums)-1:
        acumulador = acumulador * lista_nums[i]
        i += 1 
    return acumulador

#6 Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.

def pos_valor_max(lista_ints:list)->int:
    num_max = 0
    posicion_max = 0
    for i in range(len(lista_ints)):
        if lista_ints[i] > num_max:
            num_max = lista_ints[i]
            posicion_max = i
    return posicion_max

#7 Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.

def pos_valores_max(lista_ints:list)->list:
    num_max = 0
    posicion_max = 0
    lista_max = [0] * 1

    for i in range(len(lista_ints)):
        if lista_ints[i] > num_max:
            num_max = lista_ints[i]
            posicion_max = i
        
            if len(lista_max) == 1:
                lista_max[0] = posicion_max
            else:
                lista_max = [posicion_max] * 1
        elif lista_ints[i] == num_max:
            lista_max.append(i)
    return lista_max 




lista = lista_nums(5)
promedio = pos_valores_max(lista)
print(promedio)

