#4 Escribir en un archivo de texto las tablas de multiplicar del 1 al 10, cada tabla separada por una línea en blanco.

archivo = open("practicas_y_tareas/archivos/tablas.txt", "w")


for tabla in range(1,11):

    for num in range(1,11):
          linea_texto = str(tabla) + " X " + str(num) + " = " + str(num*tabla) + "\n"
          archivo.write(linea_texto)
    
    archivo.write('\n')    




archivo.close()