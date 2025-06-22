#5 Leer un archivo CSV con datos de empleados (nombre, edad, país) y mostrarlos en pantalla.
import csv
archivo = open("practicas_y_tareas/archivos/empleados.csv","r")
matriz = []
nombre_columnas = archivo.readline().strip().split(",")

for linea in archivo:
    linea = linea.rstrip("\n")
    fila = []
    valores = linea.split(",")

    for valor in valores:
        if valor.isdigit():
            fila.append(int(valor))
        else:
            fila.append(valor)
    matriz.append(fila)

print(nombre_columnas)
archivo.close()
for fila in matriz:
    print(fila)