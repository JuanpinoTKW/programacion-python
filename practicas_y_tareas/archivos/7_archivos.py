#7 Leer un archivo CSV y contar cuántas personas tienen más de 30 años.
import csv 
cont = 0
archivo = open("practicas_y_tareas/archivos/empleados.csv", "r")

for linea in archivo:
    linea = linea.rstrip("\n")
    valores = linea.split(",")

    for valor in valores:
        if valor.isdigit():
            if int(valor) > 30:
                cont += 1

archivo.close()
print(f"los mayores de 30 son: {cont}.")