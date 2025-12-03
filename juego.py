import pygame
import random

from config import *
from power_ups import aplicar_powerups, obtener_powerup_por_nivel
from ranking import pedir_nombre, mostrar_ranking

import bloques as bloques_mod


# FUNCIÓN PRINCIPAL DEL JUEGO
def iniciar_juego():
    # de este modo inicializamos pygame
    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("Assets/Sonidos/sonido_juego.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

    global FUENTE, FUENTE_TITULO, FUENTE_TEXTO
    FUENTE = pygame.font.Font(None, 50)
    FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 70)
    FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-Bold.ttf", 30)
    # IMPORTANTE: sin toda la logica de abajo se abre y se cierra rapidamente
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("ArkaLab") # constante nombre de la ventana

    nombre_icono = pygame.image.load('Assets/Intro/nombre_icono-37.png')
    pygame.display.set_icon(nombre_icono)

    nivel_actual = 1                                
    #iniciamos nivel
    bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)    
    # llamamos a crear_bloques para que sepa que nivel es
    powerups = obtener_powerup_por_nivel(nivel_actual)  #Llamamos a la funcion que indica 

    # ACA SE LLAMA AL LOOP PRINCIPAL
    loop_principal(ventana, fondo, bloques_list, nivel_actual)



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

    nivel_actual = 1
    bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)

    #POSICIONAR TAMBIEN PALETA EN EL CENTRO
    PALETA.centerx = ANCHO // 2 #ver al pasar de nivel
    PALETA.width =LARGO_PALETA
    pelota.x = PALETA.centerx - TAMANIO_PELOTA // 2
    pelota.y = PALETA.top - TAMANIO_PELOTA - 5

    pelota_en_movimiento = False

    return bloques_list, fondo, nivel_actual



# FUNCIÓN PARA IDENTIFICAR COLISION DE PELOTAS Y ACTIVAR POWERUPS
def colisionar_pelota_bloque(bloques, velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador, pelota, color_pelota, fondo, nivel_actual):
    for bloque in bloques[:]:
        if pelota.colliderect(bloque["rect"]):
            sonido_colision = pygame.mixer.Sound("Assets/Sonidos/sonido_colision_bloque2.mp3")
            sonido_colision.set_volume(0.5)  # opcional
            sonido_colision.play()
            bloques.remove(bloque)

            if bloque["powerup"] is not None:
                aplicar_powerups(bloque["powerup"], PALETA, velocidad_pelota_x, velocidad_pelota_y, color_pelota)  #Activa el powerup aleatoriamente al colisionar
            if abs(pelota.bottom -bloque["rect"].top) < 10 and velocidad_pelota_y > 0:
                velocidad_pelota_y *= -1
            elif abs(pelota.top -bloque["rect"].bottom) < 10 and velocidad_pelota_y < 0:    # funcion Abs para que rebote mas dinamicamente
                velocidad_pelota_y *= -1
            elif abs(pelota.right - bloque["rect"].left) < 10 and velocidad_pelota_x > 0:
                velocidad_pelota_x *= -1
            elif abs(pelota.left - bloque["rect"].right) < 10 and velocidad_pelota_x < 0:
                velocidad_pelota_x *= -1
            else:
                velocidad_pelota_x *= -1    #En caso de que no se pueda detectar cual es el punto de colision, vuelve en sentido contrario
                velocidad_pelota_y *= -1

            puntuacion_jugador += 5
            break

    return bloques, velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador, pelota, color_pelota, fondo, nivel_actual
# retornamos todo porque sirve para alimentar nuevamente a la funcion colisionar con el nuevo nivel



# BUCLE PRINCIPAL DEL JUEGO
def loop_principal(ventana, fondo, bloques_list, nivel_actual):
    global velocidad_pelota_x, velocidad_pelota_y, puntuacion_jugador, pelota_en_movimiento, vidas, pelota, color_pelota

    corriendo = True
    # Posicionar la pelota al inicio del juego
    pelota.x = PALETA.centerx - (TAMANIO_PELOTA // 2)
    pelota.y = PALETA.top - (TAMANIO_PELOTA + 5)

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
            velocidad_pelota_y = -abs(velocidad_pelota_y)

        # PERDER VIDAS
        vidas = perder_vidas(vidas, pelota)

        if vidas <= 0:
            pedir_nombre(ventana, ANCHO, puntuacion_jugador)
            bloques_list, fondo, nivel_actual = mostrar_pantalla_fin(ventana, "GAME OVER","reiniciar")
        
        if len(bloques_list) == 0:   
            pedir_nombre(ventana, ANCHO, puntuacion_jugador)  
            mostrar_ranking(ventana, ANCHO, ALTO)
            bloques_list, fondo, nivel_actual = mostrar_pantalla_fin(ventana, "GANASTE!", "continuar")
            nivel_actual += 1
            bloques_list, fondo = bloques_mod.crear_bloques(nivel_actual)
            

        # PUNTUACION JUGADOR
        (bloques_list,
        velocidad_pelota_y,
        velocidad_pelota_x,
        puntuacion_jugador,
        pelota,
        color_pelota, fondo, nivel_actual) = colisionar_pelota_bloque(
        bloques_list,velocidad_pelota_y,velocidad_pelota_x,puntuacion_jugador,pelota,color_pelota,fondo, nivel_actual)


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

        ventana.blit(FUENTE_TEXTO.render(f"SCORE {puntuacion_jugador}", False, BLANCO), (50, 50))
        ventana.blit(FUENTE_TEXTO.render(f"VIDAS {vidas}", False, BLANCO), (500, 50))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

pygame.quit()



