#6 Guardar en un archivo CSV los nombres y puntajes de 5 jugadores ingresados por teclado.

import csv 
nombre_columnas = ["Jugador","Puntaje"]
matriz = [["Juan",59],["Pedro",68],["Marcelo",73],["Virginia",72],["Milena",83]]
with open("practicas_y_tareas/archivos/jugadores.csv","w") as archivo:
    archivo.write(",".join(nombre_columnas) + "\n") 

    for fila in matriz:
        linea = ""
        for i in range(len(fila)):
            linea += str(fila[i])
            if i < (len(fila) - 1):
                linea += ","

        archivo.write(linea + "\n")
archivo.close()
print(archivo)