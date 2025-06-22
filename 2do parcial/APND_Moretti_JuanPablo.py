#import pygame as pg
import validaciones as vali
lista_jugadores = []
sala_1 = tuple(["Soy un bucle en Python que sigue girando mientras una condición es verdadera. ¿Quién soy?: ","while",10])
sala_2 = tuple(["Soy una estructura en Python que te dejo almacenar muchos valores, pero no me gusta el cambio: ","tupla",35])
sala_3 = tuple(["Soy una función en Python que te dice cuánto espacio ocupo, pero no en bytes, sino en cantidad de elementos: ","len()",30])
sala_4 = tuple(["Soy una palabra reservada en Python que te ayuda a tomar decisiones. Me sigues con una condición, y si es cierta, mi bloque de código se ejecuta: ","if",25])
cant_jugadores = vali.validar_jugadores("ingrese la cantidad de jugadores: ")
resultados = []

def jugar_sala(num_sala:int)->list:
    resultado = []
    print(f"Jugando sala: {num_sala}")
    match num_sala:
        case 1:
            sala_en_juego = sala_1
        case 2:
            sala_en_juego = sala_2
        case 3:
            sala_en_juego = sala_3
        case 4:
            sala_en_juego = sala_4
    respuesta = vali.validar_texto(sala_en_juego[0])
    if respuesta == sala_en_juego[1]:
        puntos = sala_en_juego[2]
        respuesta_correcta = True
    else:
        respuesta_correcta = False
        puntos = 0
    resultado.append(respuesta_correcta)
    resultado.append(puntos)

    return resultado

def mayor_puntaje(matriz:list):
    punt_mayor = 0
    for fila in range(len(matriz)):    
        if matriz[fila][1] > punt_mayor:
            punt_mayor = matriz[fila][1]
    print("* * * jugadores con mayor puntaje * * *")
    for fila in range(len(matriz)):
        if matriz[fila][1] == punt_mayor:
            print(f"jugador: {matriz[fila][0]} puntaje: {matriz[fila][1]}")

def mayor_sala(matriz:list):
    sala_mayor = 0
    for fila in range(len(matriz)):
        if matriz[fila][2] > sala_mayor:
            sala_mayor = matriz[fila][2]
    print("* * * jugadores que llegaron mas lejos * * *")
    for fila in range(len(matriz)):
        if matriz[fila][2] == sala_mayor:
            print(f"jugador: {matriz[fila][0]} sala: {matriz[fila][2]}")

def menor_sala(matriz:list):
    print("* * * jugadores que no superaron la sala 1 * * *")
    for fila in range(len(matriz)):
        if matriz[fila][1] == 0:
             print(f"jugador: {matriz[fila][0]}")

for i in range(1,cant_jugadores+1):
    nombre_jugador = vali.validar_texto(f"ingrese el nombre del jugador {i}: ")
    intentos = 2
    puntaje = 0
    sala_actual = 1
    sala_superada = False
    while intentos > 0 and sala_superada == False and sala_actual < 5:
        acerto = jugar_sala(sala_actual)
        if acerto[0] == True:
            print("respuesta correcta!!")
            sala_actual += 1
            intentos = 2
            puntaje += acerto[1]
        else:
            print("Respuesta incorrecta!!")
            intentos -= 1
    resultados.append([nombre_jugador,puntaje,sala_actual])



mayor_puntaje(resultados)
mayor_sala(resultados)
menor_sala(resultados)
    #print(f"el jugador {nombre_jugador} obtuvo {puntaje} puntos.")