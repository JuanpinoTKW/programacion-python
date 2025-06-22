#3 Leer un archivo de texto y contar cuántas líneas tiene.
cont = 0
archivo = open("practicas_y_tareas/archivos/archivo.txt", "r+")
lista_lineas = archivo.readlines()
for linea in lista_lineas:
    cont += 1
archivo.close()
print(f"la cantidad de lineas del archivo es: {cont} {len(lista_lineas)}")