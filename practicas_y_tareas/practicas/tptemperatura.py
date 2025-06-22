'''
Enunciado: Conversión de Temperatura con Múltiples Opciones
Desarrolla un programa en Python que permite convertir temperaturas entre diferentes unidades. El usuario debe poder elegir entre las siguientes:
Celsius y Fahrenheit
Fahrenheit y Celsius
Celsius y Kelvin
El programa debe solicitar al usuario:
La opción de con La temperatura
Luego, debe mostrar el resultado de la conversión en la unidad correspondiente.
Fórmulas de conversión:
Celsius y Fahrenheit :
F = 9/5 C + 32
Fahrenheit y Celsius :
C = 5/9 ( F−32)
Celsius y Kelvin :
K = C + 273.1
Si el usuario elige una opción incorrecta, el programa debe mostrar un mensaje de error.
'''
temperatura_celcius = int(input("ingrese una temperatura en grados celcius: "))
temperatura_fahr = int(input("ingrese una temperatura en grados fahrenheit: "))
temperatura_kelvin = int(input("ingrese una temperatura en grados celcius: "))
celcius_fahr = (temperatura_celcius * 9/5) + 32
fahr_celcius = (temperatura_fahr - 32) * 5/9
celcius_kelvin = temperatura_celcius + 273
print(f"la temperatura de grados celcius a fahrenheit es {celcius_fahr}, de fahrenheit a celcius es {fahr_celcius} y de celcius a kelvin son {celcius_kelvin}")