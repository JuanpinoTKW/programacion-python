"""
Una tienda de ropa cuenta con 5 categorías de productos , con código de categoría van desde el  11 al 15 (por ejemplo 11 es pantalones, 
12 es remeras, etc) . 
Cada categoría tiene 10 productos, con código de categoría numerado del 1 al 10 ,  lo que da un total de 50 productos en el inventario. 
La tienda tiene 10 empleados, cada uno identificado con un número de empleado único.(pre cargar la lista de empleados con valores de número de 
empleado del 101 al 110)

Para llevar un control eficiente del inventario, se necesita desarrollar un software que permita gestionar y analizar el stock de productos de 
la tienda.

🔹 Funcionalidades del Programa

El sistema debe presentar un menú de opciones con las siguientes funciones:

1 Cargar entrada de inventario (la cantidad de unidades ingresadas de un codigo de producto para una categoría )
 El empleado debe identificarse ingresando su número de empleado.
Se debe validar que el número de empleado ingresado exista dentro de la lista de empleados generada previamente.
Si el empleado existe, podrá registrar las entradas de productos al inventario, indicando la categoría (del 11 al 15)  y el código del producto.
(del 1 al 10)
Un empleado puede registrar varias entradas de productos durante el día en distintas categorías.

2 Mostrar el inventario de productos
 Presentar una lista de todos los productos en inventario, organizada por categorías, junto con la cantidad disponible de cada uno.

3 Calcular y mostrar el stock total por cada categoría
 Sumar y mostrar la cantidad total de productos en stock por cada categoría.

4 Calcular y mostrar el código de categoría y de producto que tiene mayor Stock

5 Ordenar (con algoritmo burbuja) y  Mostrar la lista de empleados ordenada por código de empleado de forma descendente

6 Calcular y mostrar el stock total
Mostrar el total general de todos los productos en el inventario.

7- Calcular y mostrar el stock total para un código de producto que ingrese el usuario (pedir el ingreso y validarlo)

8- Salir
"""

empleados = [101,102,103,104,105,106,107,108,109,110]