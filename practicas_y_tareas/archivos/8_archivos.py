#8 Crear un archivo CSV con los datos de 5 productos (nombre, precio, stock) y luego leerlo y mostrar los productos con stock menor a 10.
import csv
menor_10 = 0
archivo = open("practicas_y_tareas/archivos/productos.csv", "r")
matriz = []
for linea in archivo:
    linea = linea.rstrip("\n")
    fila = []
    valores = linea.split(",")


    for valor in valores:
        if valor.isdigit():
            fila.append(int(valor))
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if int(valor) < 10:
                        menor_10 += 0
        else:
            fila.append(valor)
    matriz.append(fila)
archivo.close()
print(matriz)
print(f"los productos con el stock menor a 10 son: {menor_10}.")