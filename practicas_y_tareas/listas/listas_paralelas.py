import sys
sys.path.append("C:/Users/juanp/OneDrive/Escritorio/python/practicas y tareas/validaciones")
import validaciones

"""
Cargar en una lista los nombres de 5 personas y en otra lista paralela sus edades. 
Pedir una edad y mostrar los nombres de todas las personas que tengan esa edad.

lista_nombre = [""] * 5
lista_edad = [0] * 5

for i in range(len(lista_nombre)):
    lista_nombre[i] = input("ingrese un nombre: ")
    lista_edad[i] = int(input("ingrese una edad: "))

edad_buscar = int(input("ingrese la edad a buscar: "))
for i in range(len(lista_edad)):
    if edad_buscar == lista_edad[i]:
        print(lista_nombre[i])

Cargar en una lista los nombres de 5 alumnos y en otra lista paralela las notas que obtuvieron. 
Mostrar el nombre del alumno con la nota más alta.

lista_alumnos = [""] * 5
lista_notas = [0] * 5
nota_max = 0
alum_max = ""

for i in range(len(lista_alumnos)):
    lista_alumnos[i] = input("ingrese el nombre del alumno: ")
    lista_notas[i] = float(input("ingrese la calificacion: "))

for i in range(len(lista_notas)):
    if nota_max < lista_notas[i]:
        nota_max = lista_notas[i]
        alum_max = lista_alumnos[i]

print(f"el alumno con la mayor calificacion es {alum_max} con {nota_max}")

Cargar en una lista los nombres de 6 empleados y en otra lista paralela sus sueldos. 
Mostrar el sueldo promedio de los empleados, y el nombre del empleado con sueldo más bajo

lista_empleados = [""] * 6
lista_sueldos = [0] * 6
acumulador = 0
sueldo_menor = float('inf')
empleado_menor = ""

for i in range(len(lista_sueldos)):
    lista_empleados[i] = input("ingrese el nombre del empleado: ")
    lista_sueldos[i] = int(input("ingrese el sueldo ganado: "))

for i in range(len(lista_sueldos)):
    acumulador += lista_sueldos[i]
    if lista_sueldos[i] < sueldo_menor:
        sueldo_menor = lista_sueldos[i]
        empleado_menor = lista_empleados[i]

promedio = acumulador / 6
print(f"el empleado con el sueldo menor es {empleado_menor} que gano {sueldo_menor} y el promedio de los sueldos es de {promedio}")

Cargar en una lista los nombres de 5 artículos y en otra lista paralela la cantidad de unidades en stock. 
Mostrar el nombre del artículo con menos stock disponible.

lista_productos = [""] * 5
lista_stock = [0] * 5
stock_menor = float('inf')
prod_menor = ""

for i in range(len(lista_stock)):
    lista_productos[i] = input("ingrese un producto: ")
    lista_stock[i] = int(input("ingrese el numero de stock del producto: "))
for i in range(len(lista_stock)):
    if lista_stock[i] < stock_menor:
        stock_menor = lista_stock[i]
        prod_menor = lista_productos[i]

print(f"el producto con el menor stock es {prod_menor} que tiene {stock_menor} unidades")

Cargar en una lista los nombres de 5 materias y en otra lista paralela la nota obtenida en cada una (entre 1 y 10, validar el ingreso).
Mostrar:
a)El nombre de la materia con la nota más alta.
b)Cuántas materias tienen nota mayor a 7.
c) si hubo alguna nota que sea 10 (si o no)
"""

lista_materias = [""] * 5
lista_notas = [0] * 5
nota_max = 0
materia_max = ""
mayor_a_7 = 0
mayor_a_10 = False

for i in range(len(lista_notas)):
    lista_materias[i] = validaciones.validar_texto("ingrese el nombre de una materia: ")
    lista_notas[i] = validaciones.validar_entero_pos("ingrese la nota obtenida en la materia: ")

for i in range(len(lista_notas)):
    if nota_max < lista_notas[i]:
        nota_max = lista_notas[i]
        materia_max = lista_materias[i]
    
    if lista_notas[i] > 7:
        mayor_a_7 += 1
        if lista_notas[i] == 10:
            mayor_a_10 = True

if mayor_a_10 == True:
    mensaje = "Si hay"
else:
    mensaje = "No hay"
        
print(f"la materia con la nota mas alta es {materia_max} con {nota_max}; {mensaje} materias con 10; y las materias con nota mayor a 7 son {mayor_a_7}")
