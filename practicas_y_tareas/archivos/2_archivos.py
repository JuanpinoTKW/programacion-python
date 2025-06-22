#2 Guardar en un archivo de texto los nombres de 5 personas ingresados por teclado.

import csv
archivo = open("practicas_y_tareas/archivos/archivo.txt", "w+")
lista_nombres = ['nombre 1\n'
                'nombre 2\n',
                'nombre 3\n',
                'nombre 4\n',
                'nombre 5\n',
                'nombre 6\n']
archivo.writelines(lista_nombres)
archivo.close()
