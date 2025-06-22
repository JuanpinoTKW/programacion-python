#5. Dada la lista tareas = ["limpiar", "cocinar", "estudiar"], sacá la última tarea de esta lista, 
# y agregala a la lista completadas = [“hacer compras”].

tareas = ["limpiar", "cocinar", "estudiar"]
completadas = ["hacer compras"]
completadas += tareas.pop(2)
print(tareas)
print(completadas)