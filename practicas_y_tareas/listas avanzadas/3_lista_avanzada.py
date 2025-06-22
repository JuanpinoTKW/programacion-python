#3. Combiná la lista original = [10, 20, 60, 90] con nuevos = [30, 40, 50], de modo que todos los elementos queden en una sola lista.

numeros_a = [10,20,60,90]
numeros_b = [30,40,50]

numeros_a.extend(numeros_b)
print(numeros_a)