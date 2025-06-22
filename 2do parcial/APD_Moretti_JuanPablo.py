import pygame as py
import validaciones as vali

py.init()
py.display.set_caption("Sala de Escape de Programadores")

ANCHO = 800
ALTO = 500
# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
AMARILLO = (255,255,0)

ventana = py.display.set_mode((ANCHO,ALTO))
fuente = py.font.SysFont("arial", 32)
fuente_pregunta = py.font.SysFont("arial", 25)

texto = ""
input_activo = False
rect_input = py.Rect(200, 250, 300, 40)  # Posición y tamaño del cuadro de texto
color_input = BLANCO

# Reloj para controlar el framerate
timer = py.time.Clock()

# Configuración del temporizador
tiempo_total = 10  # Tiempo inicial en segundos
tiempo_inicio = py.time.get_ticks()  # Tiempo inicial
juego_terminado = False

corriendo = True
while corriendo:
    for evento in py.event.get():
        if evento.type == py.QUIT:
            corriendo = False
         # Detectar clic en el cuadro de texto
        if evento.type == py.MOUSEBUTTONDOWN:
            if rect_input.collidepoint(evento.pos):
                input_activo = True
                color_input = BLANCO
            else:
                input_activo = False
                color_input = GRIS
        # Detectar clic en el cuadro de texto
        if evento.type == py.MOUSEBUTTONDOWN:
            if rect_input.collidepoint(evento.pos):
                input_activo = True
                color_input = BLANCO
            else:
                input_activo = False
                color_input = GRIS
        # Capturar teclas si el input está activo
        if evento.type == py.KEYDOWN and input_activo:
            if evento.key == py.K_RETURN:
                print("Texto ingresado:", texto)  # Acción al presionar Enter
                texto = ""  # Limpiar el texto
            elif evento.key == py.K_BACKSPACE:
                texto = texto[:-1]  # Borrar el último carácter
            else:
                # Agregar el carácter si es imprimible
                if evento.unicode.isprintable():
                    texto += evento.unicode
    
    # Limpiar la pantalla
    ventana.fill(NEGRO)
    if not juego_terminado:
        # Calcular el tiempo restante
        tiempo_transcurrido = (py.time.get_ticks() - tiempo_inicio) // 1000  # En segundos
        tiempo_restante = max(0, tiempo_total - tiempo_transcurrido)  # Tiempo restante

        # Renderizar el texto del temporizador
        texto_temporizador = fuente.render(f"Tiempo: {tiempo_restante} s", True, (AMARILLO))  # Texto amarillo
        rect_texto_temporizador = texto_temporizador.get_rect(center=(ventana.get_width() // 7, 450))
        ventana.blit(texto_temporizador, rect_texto_temporizador)

        # Verificar si el tiempo se acabó
        if tiempo_restante == 0:
            juego_terminado = True
    else:
        # Mostrar mensaje de fin
        texto_fin = fuente.render("¡Tiempo terminado!", True, (255, 0, 0))  # Texto rojo
        rect_texto_fin = texto_fin.get_rect(center=(ventana.get_width() // 2, ventana.get_height() // 3))
        ventana.blit(texto_fin, rect_texto_fin)

    # Escribir Pregunta
    texto_pregunta1 = fuente_pregunta.render("Soy una palabra reservada en Python que te ayuda a tomar decisiones", True, BLANCO)
    ventana.blit(texto_pregunta1, (50, 100))

    texto_pregunta2 = fuente_pregunta.render("Me sigues con una condición, y si es cierta, mi bloque de código se ejecuta", True, BLANCO)
    ventana.blit(texto_pregunta2, (50, 50))
    # Dibujar el cuadro de texto
    py.draw.rect(ventana, color_input, rect_input, 2)

    # Renderizar el texto
    superficie_texto = fuente.render(texto, True, BLANCO)
    ventana.blit(superficie_texto, (rect_input.x + 5, rect_input.y + 5))

    # Asegurar que el texto no se salga del cuadro
    rect_input.w = max(380, superficie_texto.get_width() + 10)

    
    # Actualizar la pantalla
    py.display.flip()


        #py.display.update()
    #texto = fuente.render("hola que tal?", True, AMARILLO)
    #ventana.blit(texto, (100,100))
    #py.draw.rect(ventana, (255, 0, 0), (300, 150, 300, 300), 2)  # Color rojo, grosor 2

py.quit()