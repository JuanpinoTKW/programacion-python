'''
Realizar un programa que permita que el usuario ingrese todos los números que desee hasta que ingrese 0 (0 es fin de datos) . 
Una vez finalizada la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande. el numero menor
'''
num = 1
cont = 0
cont_neg = 0
suma = 0
suma_neg = 0
num_grande = 0
num_menor = 0

while num != 0:

# for i in range(1,9999999):
    num = int(input("ingrese los numeros que usted desee. Para finalizar ingrese '0': "))
    if num < 0:
        suma_neg += num
        cont_neg += 1
        if num < num_menor:
            num_menor = num
    elif num > 0:
        suma += num 
        cont += 1
        if num > num_grande:
            num_grande = num
    elif num == 0:
        break 
promedio = suma / cont 

print(f"la suma acumulada de los numeros negativos es {suma_neg}, de los positivos es {suma}, la cantidad de numeros negativos es {cont_neg} y de positivos es {cont}. el promedio de los numeros positivos es {promedio}, el numero mayor es {num_grande} y el menor es {num_menor}")
        
    
