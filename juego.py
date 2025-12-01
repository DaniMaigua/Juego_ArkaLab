import pygame # importamos la libreria. Primero la debemos instalar
import random

from constantes import *
from power_ups import * #ver - creo que no importo nada puntual, porque bloques esta en bloques.py
# from bloques import *
import bloques as bloques_mod


# # FUENTE = pygame.font.Font(None, 50)
# FUENTE = None

# pelota = pygame.Rect (PALETA.centerx - (TAMANIO_PELOTA // 2), PALETA.top - (TAMANIO_PELOTA + 5), TAMANIO_PELOTA, TAMANIO_PELOTA)
# color_pelota = {"valor": (100, 100, 200)}


# FUNCIÓN PRINCIPAL DEL JUEGO
def iniciar_juego():
    # de este modo inicializamos pygame
    pygame.init()

    global FUENTE, FUENTE_TITULO, FUENTE_TEXTO
    FUENTE = pygame.font.Font(None, 50)
    FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 70)
    FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-Bold.ttf", 30)
    #IMPORTANTE: sin toda la logica de abajo se abre y se cierra rapidamente
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("ArkaLab") # constante nombre de la ventana

    nombre_icono = pygame.image.load('Assets/Intro/nombre_icono-37.png')
    pygame.display.set_icon(nombre_icono)

    nivel_actual = 1                                
    #iniciamos nivel
    bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)    
    # llamamos a crear_bloques para que sepa que nivel es

    # ACA SE LLAMA AL LOOP PRINCIPAL
    loop_principal(ventana, fondo, bloques_list, nivel_actual)



# def reiniciar_juego(pelota,keys, vidas, puntuacion_jugador):

#     if keys[pygame.K_SPACE]:
#         vidas = 3
#         puntuacion_jugador = 0

#         # pelota.x = (ANCHO // 2) - (TAMANIO_PELOTA // 2)
#         # pelota.y = PALETA.top - TAMANIO_PELOTA - 5

#         # Reubicar pelota siempre encima de la paleta antes de soltarla
#         pelota.x = PALETA.centerx - TAMANIO_PELOTA // 2
#         pelota.y = PALETA.top - TAMANIO_PELOTA - 5

#         # bloques = crear_bloques()
#         bloques, fondo = crear_bloques(nivel_actual)

#         return vidas, puntuacion_jugador, bloques #solo retorna valores actualizados cuando retorno space

#     return vidas, puntuacion_jugador, bloques


def perder_vidas(vidas, pelota):
    # Si la pelota pasó el borde inferior
    if pelota.bottom >= ALTO:
        vidas -= 1

        # reiniciar paleta -> CENTRAR LA PALETA
        PALETA.centerx = ANCHO // 2
        PALETA.width = LARGO_PALETA

        # Reiniciar pelota -> IMPORTANTE, COORDENADAS DE POSICION INICIAL DE PELOTA
        pelota.x = PALETA.centerx - TAMANIO_PELOTA // 2
        pelota.y = PALETA.top - TAMANIO_PELOTA - 5

        # Detengo el movimiento
        global pelota_en_movimiento
        pelota_en_movimiento = False

    return vidas


def mostrar_pantalla_fin(ventana, mensaje, mensaje_secundario):
    global vidas, puntuacion_jugador, pelota_en_movimiento, pelota

    # Creamos textos
    texto_principal = FUENTE_TITULO.render(f"{mensaje}", False, COLOR_PALETA)
    texto_secundario = FUENTE_TEXTO.render(f"Presiona SPACE para {mensaje_secundario}", True, COLOR_PALETA)

    rect_fondo = pygame.Surface((450, 150), pygame.SRCALPHA)
    rect_fondo.fill((0, 0, 0, 200)) 

    # bliteamos en pantalla 
    ventana.blit(rect_fondo, (150,230))
    ventana.blit(texto_principal, (160, 240))
    ventana.blit(texto_secundario, (195, 315))

    # ventana.blit(texto_principal, (ANCHO//2 - texto_principal.get_width()//2, ALTO//2 - 50))

    pygame.display.flip()

    # Esperar presionar tecla SPACE
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                esperando = False

        pygame.time.Clock().tick(60)

    # Reiniciar valores del juego
    vidas = 3
    puntuacion_jugador = 0
    # bloques, fondo = crear_bloques()
    nivel_actual = 1
    bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)

    #POSICIONAR TAMBIEN PALETA EN EL CENTRO
    PALETA.centerx = ANCHO // 2 #ver al pasar de nivel
    PALETA.width =LARGO_PALETA
    pelota.x = PALETA.centerx - TAMANIO_PELOTA // 2
    pelota.y = PALETA.top - TAMANIO_PELOTA - 5

    pelota_en_movimiento = False

    return bloques_list, fondo, nivel_actual




# BUCLE PRINCIPAL DEL JUEGO
def loop_principal(ventana, fondo, bloques_list, nivel_actual):
    global velocidad_pelota_x, velocidad_pelota_y
    global puntuacion_jugador, pelota_en_movimiento, vidas
    global pelota, color_pelota
    corriendo = True
    # Posicionar la pelota al inicio del juego
    pelota.x = PALETA.centerx - (TAMANIO_PELOTA // 2)
    pelota.y = PALETA.top - (TAMANIO_PELOTA + 5)
    #hacer funcion

    pelota_en_movimiento = False

    while corriendo:
    # EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #APRETAR LA X
                corriendo = False

            if event.type == pygame.KEYDOWN: #presionar tecla
                if event.key == pygame.K_SPACE and not pelota_en_movimiento:
                    
                    # Reubicar pelota siempre encima de la paleta antes de soltarla
                    pelota.x = PALETA.centerx - TAMANIO_PELOTA // 2
                    pelota.y = PALETA.top - TAMANIO_PELOTA - 5
                    # PALETA.x = PALETA.centerx
                    # - TAMANIO_PELOTA // -> ver si pone pelota en el centro

                    velocidad_pelota_x = random.choice([-5, 5])
                    velocidad_pelota_y = -5  # siempre hacia arriba
                    pelota_en_movimiento = True


        # Movimiento de paleta
        keys = pygame.key.get_pressed() #mantener presionado

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and PALETA.right < ANCHO:
            PALETA.x += VELOCIDAD_PALETA

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and PALETA.left > 0:
            PALETA.x -= VELOCIDAD_PALETA


        # COLISIONES CON BORDES
        if pelota.top <= 0:
            velocidad_pelota_y *= -1 #indica, si la pelota toca el top, que invierta el signo, de positivo a negativo

        if pelota.left <= 0 or pelota.right >= ANCHO:
            velocidad_pelota_x *= - 1 #SOLO EN EJE X

        # COLISIONES CON PALETA
        if pelota.colliderect(PALETA):
            # velocidad_pelota_y *= -1
            velocidad_pelota_y = -abs(velocidad_pelota_y)

            # velocidad_pelota_x *= -1 #-> ver como funciona

        # PERDER VIDAS
        vidas = perder_vidas(vidas, pelota)

        if vidas <= 0:
            vidas == 0
            bloques_list, fondo, nivel_actual = mostrar_pantalla_fin(ventana, "GAME OVER","reiniciar")
        
        if len(bloques_list) == 0:     
            bloques_list, fondo, nivel_actual = mostrar_pantalla_fin(ventana, "GANASTE!", "continuar")
            nivel_actual += 1
            bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)

        # PUNTUACION JUGADOR
        # actualizar_powerups(ventana, powerups, PALETA, velocidad_pelota_x, velocidad_pelota_y)
        (bloques_list,
        velocidad_pelota_y,
        velocidad_pelota_x,
        puntuacion_jugador,
        pelota,
        color_pelota, fondo, nivel_actual) = bloques_mod.colisionar_pelota_bloque(
        bloques_list,velocidad_pelota_y,velocidad_pelota_x,puntuacion_jugador,pelota,color_pelota,fondo, nivel_actual)

        # puntuacion_jugador = colisionar_pelota_bloque(bloques, velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador, pelota, color_pelota)

        # MOVIMIENTO DE LA PELOTA
        if pelota_en_movimiento:
            pelota.x += velocidad_pelota_x
            pelota.y += velocidad_pelota_y


        # DIBUJADO EN PANTALLA
        ventana.blit(fondo, (0, 0))

        #creacion del rectangulo (ubicacion, color, objeto -> un rectangulo)
        pygame.draw.rect(ventana,COLOR_PALETA, PALETA)
        pygame.draw.rect(ventana, (0, 0, 0), PALETA, 1) # Borde de la paleta
        #LUEGO dibujamos la pelota
        pygame.draw.ellipse(ventana, color_pelota["valor"], pelota)
        pygame.draw.ellipse(ventana, (0, 0, 0), pelota, 1) # Borde de la pelota

        for bloque in bloques_list:
            ventana.blit(bloque["img"], bloque["rect"])

        ventana.blit(FUENTE_TEXTO.render(f"{ puntuacion_jugador}", False, COLOR_PALETA), (50, 50))
        ventana.blit(FUENTE.render(f"{ vidas}", False, COLOR_PALETA), (500, 50))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

pygame.quit()



