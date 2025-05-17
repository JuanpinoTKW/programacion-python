'''
Escribe un programa que calcule el número de horas de estudio recomendadas para un estudiante. El programa debe pedir al usuario que ingrese el 
número de materias (entero positivo), el promedio de calificaciones (número decimal) y su tipo de desempeño (alto, medio o bajo).

El programa debe calcular el número de horas recomendadas de estudio por semana:

Si el promedio es mayor o igual a 9 y el tipo de desempeño es "alto", el estudiante debe estudiar 5 horas por materia.
Si el promedio es menor a 9 y el tipo de desempeño es "medio", el estudiante debe estudiar 7 horas por materia.
Si el desempeño es "bajo", el estudiante debe estudiar 10 horas por materia.
Si el número de materias es mayor a 5, se incrementa 1 hora adicional de estudio por materia.
Finalmente, el programa debe mostrar cuántas horas debe estudiar el usuario por materia y el total de horas de estudio por semana.
'''
materias = int(input("Ingrese el número de materias del semestre: "))
promedio = float(input("Ingrese su promedio de calificaciones: "))
desempeño = input("Ingrese su tipo de desempeño (alto/medio/bajo): ")

horas_estudio = None

if promedio >= 9 and desempeño == "alto":
    horas_estudio = 5
elif promedio < 9 and desempeño == "medio":
    horas_estudio = 7
elif desempeño == "bajo":
    horas_estudio = 10

if materias > 5:
    horas_estudio += 1

total_horas = horas_estudio * materias

print(f"Debe estudiar {horas_estudio} horas por materia por semana.")
print(f"El total de horas de estudio por semana es {total_horas}.")
