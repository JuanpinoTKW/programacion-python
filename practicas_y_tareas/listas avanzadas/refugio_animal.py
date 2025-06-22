import copy
#1. Creá la lista vacía animales.

animales = []

#2. Agregá animales: Agregá "Luna", "Simón" y "Nina".

animales.append("Luna")
animales.append("Simon")
animales.append("Nina")

#3. Insertá un nuevo animal en la segunda posición: Insertá "Toby".

animales.insert(1, "Toby")

#4. Recibís un lote nuevo de animales, agregá a  ["Milo", "Mora", "Felipe"].

animales_nuevos = ["Milo", "Mora", "Felipe"]
animales.extend(animales_nuevos)


#5. Un adoptante se lleva a "Mora", eliminalo de la lista.

animales.remove("Mora")

#6. Otro adoptante pide al último animal de la lista, sacalo e informale al adoptante qué animal es al sacarlo.

adoptado = animales.pop(5)
print(f"el animal adopatado es {adoptado}")

#7. Ups, el sistema colapsó y necesitás reiniciar la lista de animales, vaciala.

animales.clear()
print(animales)

#8. Volvé a cargar los animales originales (podés copiar y pegar los pasos anteriores) y encontrá la posición de "Simón". Informala.

animales.append("Luna")
animales.append("Simon")
animales.append("Nina")
posicion = animales.index("Simon")
print(f"Simon esta en la posicion {posicion}")

#9. Ordená los animales alfabéticamente.

animales.sort()

#10. Invertí el orden.

animales.reverse()

#11. Hacé una copia superficial de la lista en una nueva variable copia_refugio.

copia_refugio = []
copia_refugio = animales.copy()

print(copia_refugio)

#12. Luego creá una copia profunda (deep copy) en una nueva variable copia_segura usando el módulo copy. 
# Simulá que modificás una sublista en la original para ver la diferencia.

copia_segura = []
copia_segura = copy.deepcopy(animales)

print(copia_segura)