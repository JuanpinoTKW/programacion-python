import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana
pantalla = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Temporizador Regresivo")

# Definir la fuente
fuente = pygame.font.SysFont('Arial', 36)

# Reloj para controlar el framerate
reloj = pygame.time.Clock()

# Configuración del temporizador
tiempo_total = 10  # Tiempo inicial en segundos
tiempo_inicio = pygame.time.get_ticks()  # Tiempo inicial
juego_terminado = False

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Limpiar la pantalla
    pantalla.fill((255, 255, 255))  # Fondo blanco

    if not juego_terminado:
        # Calcular el tiempo restante
        tiempo_transcurrido = (pygame.time.get_ticks() - tiempo_inicio) // 1000  # En segundos
        tiempo_restante = max(0, tiempo_total - tiempo_transcurrido)  # Tiempo restante

        # Renderizar el texto del temporizador
        texto_temporizador = fuente.render(f"Tiempo: {tiempo_restante} s", True, (0, 0, 0))  # Texto negro
        rect_texto_temporizador = texto_temporizador.get_rect(center=(pantalla.get_width() // 2, 50))
        pantalla.blit(texto_temporizador, rect_texto_temporizador)

        # Verificar si el tiempo se acabó
        if tiempo_restante == 0:
            juego_terminado = True
    else:
        # Mostrar mensaje de fin
        texto_fin = fuente.render("¡Tiempo terminado!", True, (255, 0, 0))  # Texto rojo
        rect_texto_fin = texto_fin.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() // 2))
        pantalla.blit(texto_fin, rect_texto_fin)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el framerate
    reloj.tick(60)  # 60 FPS

# Salir de Pygame
pygame.quit()