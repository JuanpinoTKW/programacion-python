#8. La lista personas = [["Ana", 25], ["Luis", 30]] contiene sublistas. Hacés una copia de esa lista y luego cambiás personas[0][1] a 99. 
# Sin embargo, la copia también se ve afectada.
import copy

personas = [["Ana", 25], ["Luis", 30]]
copia = []
copia = personas.copy()
copia[0][1] = 99

print(personas)
print(copia)