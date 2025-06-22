#Leer un archivo de texto y mostrar su contenido línea por línea por pantalla.
import csv

archivo = open("practicas_y_tareas/archivos/archivo.txt", "r")
texto = archivo.read()
archivo.close()

print(texto)