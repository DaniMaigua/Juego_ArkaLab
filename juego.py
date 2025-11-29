import pygame # importamos la libreria. Primero la debemos instalar
import random
# import os

# from menu import *
from constantes import *

# from bloques import pared_bloques

# de este modo inicializamos pygame
pygame.init()


# ============================================================
# FUNCIÓN PRINCIPAL DEL JUEGO
# ============================================================
def iniciar_juego():

    # --------------------------
    # VARIABLES DEL JUEGO
    # --------------------------
    velocidad_pelota_x = 5
    velocidad_pelota_y = -5
    puntuacion_jugador = 0
    pelota_en_movimiento = False
    vidas = 3

    #IMPORTANTE: sin toda la logica de abajo se abrira y se cerrara rapidamente
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("ArkaLab") # constante nombre de la ventana

    fondo = pygame.image.load("Assets/Fondo/Fondo_pygame.png").convert()

    # =================================================================================
    # PARED BLOQUES
    # =================================================================================

    # Diccionario de bloques -> util para power ups
    imagenes_bloques = {
        "Na": pygame.image.load("Assets/Elementos/Celeste/celeste_alcalino_hidrogeno.png"),
        "H": pygame.image.load("Assets/Elementos/Celeste/celeste_alcalino_sodio.png"),
        "B": pygame.image.load("Assets/Elementos/Amarillo/amarillo_metaloide_boro-22.png"),
        "Si": pygame.image.load("Assets/Elementos/Amarillo/amarillo_metaloide_silicio-23.png"),
        "P": pygame.image.load("Assets/Elementos/Azul/azul_lantanido_fosforo-20.png"),
        "Th": pygame.image.load("Assets/Elementos/Naranja/naranja_actinido_torio-14.png"),
        "U": pygame.image.load("Assets/Elementos/Naranja/naranja_actinido_uranio-15.png"),
        "He": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_helio-17.png"),
        "Ne": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_neon-18.png"),
        "Kr": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_kripton-19.png"),
        "Ce": pygame.image.load("Assets/Elementos/Verde_Agua/verde_agua_nometal_cerio-16.png"),
        "Cr": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_cromo-11.png"),
        "Fe": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_hierro-12.png"),
        "Mt": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_meitnerio-13.png"),
        "Ti": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_titanio-10.png"),
    }

    imagenes_bloques = [
        pygame.transform.scale(imagenes_bloques[img_key],(ANCHO_BLOQUE, ALTO_BLOQUE))
        for img_key in imagenes_bloques
    ]

    bloques = []

    # ------------------------------------------------------
    # FUNCIÓN PARA CREAR LA MATRIZ DE BLOQUES
    # ------------------------------------------------------
    def crear_bloques():
        bloques.clear()

        ancho_matriz_bloques = COLUMNAS * (ANCHO_BLOQUE + ESPACIO) - ESPACIO
        offset_x = (ANCHO - ancho_matriz_bloques) // 2 #centrarlo segun tamaño matriz
        offset_y = 150  # BAJAR LOS BLOQUES

        for fila in range(FILAS):
            for col in range(COLUMNAS):
                x = offset_x + col * (ANCHO_BLOQUE + ESPACIO)
                y = offset_y + fila * (ALTO_BLOQUE + ESPACIO)

                rect = pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE)

                # Imagen al azar (de las disponibles)
                img = random.choice(imagenes_bloques)

                #DICCIONARIO -> rectangulo e imagen
                bloques.append({
                    "rect": rect,
                    "img": img
                })

    crear_bloques()


    # =================================================================================
    # PELOTA
    # =================================================================================

    # Tu comentario intacto
    pelota = pygame.Rect (PALETA.centerx - (TAMANIO_PELOTA // 2), PALETA.top - (TAMANIO_PELOTA -5), TAMANIO_PELOTA, TAMANIO_PELOTA)

    # =================================================================================
    # PANTALLA
    # =================================================================================

    FUENTE = pygame.font.Font(None, 50)
    corriendo = True


    # ============================================================
    # FUNCIÓN: PERDER VIDAS
    # ============================================================
    def reiniciar_juego():

        if keys[pygame.K_SPACE]:
            vidas = 3
            puntuacion_jugador = 0
            pelota.x = (ANCHO // 2) - (TAMANIO_PELOTA // 2)
            pelota.y = 650 - (TAMANIO_PELOTA // 2)
            crear_bloques()
            return vidas, puntuacion_jugador
        

    def perder_vidas (vidas):# PERDER VIDA

        FUENTE.render(f"Vidas: {vidas}", False, COLOR_PALETA)
        if pelota.bottom >= ALTO:
            vidas -= 1
            # Reiniciar pelota -> IMPORTANTE, COORDENADAS DE POSICION INICIAL DE PELOTA
            if vidas == 0:
                FUENTE.render("Game Over", False, COLOR_PALETA)
                reiniciar_juego()
        return vidas
    

    def colisionar_pelota_bloque(bloques, velocidad_pelota_y, puntuacion_jugador):
            for bloque in bloques[:]:
                if pelota.colliderect(bloque["rect"]):
                    bloques.remove(bloque)
                    velocidad_pelota_y *= -1
                    puntuacion_jugador += 5
                    break
            return puntuacion_jugador

    # ============================================================
    # BUCLE PRINCIPAL DEL JUEGO (TU PREGUNTA)
    # Sí: este es EL WHILE PRINCIPAL
    # ============================================================
    while corriendo:

        # --------------------------
        # EVENTOS
        # --------------------------
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

                    # # ejes de movimiento de la pelota
                    # velocidad_pelota_x = 5 #* random.choice([1, -1]) 
                    # velocidad_pelota_y = -5
                    pelota_en_movimiento = True
                    # pelota.x += velocidad_pelota_x * random.choice([-1])
                    # pelota.y += velocidad_pelota_y * random.choice([1])

            # if event.key == pygame.K_SPACE and not pelota_en_movimiento:


    # pelota_en_movimiento = True


            # Movimiento de paleta
            keys = pygame.key.get_pressed() #mantener presionado

            if keys[pygame.K_d] and PALETA.right < ANCHO:
                PALETA.x += VELOCIDAD_PALETA
            if keys[pygame.K_a] and PALETA.left > 0:
                PALETA.x -= VELOCIDAD_PALETA


        # ============================================================
        # COLISIONES CON BORDES
        # ============================================================
        if pelota.top <= 0:
            velocidad_pelota_y *= -1
        if pelota.left <= 0 or pelota.right >= ANCHO:
            velocidad_pelota_x *= - 1

        # ============================================================
        # COLISIONES CON PALETA
        # ============================================================
        if pelota.colliderect(PALETA):
            velocidad_pelota_y *= -1
            velocidad_pelota_x *= -1 #-> ver como funciona


        # ============================================================
        # FUNCIÓN: REINICIAR JUEGO
        # ============================================================

        vidas_disponibles = perder_vidas(vidas) #variable


        # ============================================================
        # FUNCIÓN: COLISIÓN PELOTA-BLOQUE
        # ============================================================
        
                
        puntuacion_jugador = colisionar_pelota_bloque(bloques, velocidad_pelota_y, puntuacion_jugador)


        # ============================================================
        # MOVIMIENTO DE LA PELOTA
        # ============================================================
        if pelota_en_movimiento:
            pelota.x += velocidad_pelota_x
            pelota.y += velocidad_pelota_y


        # ============================================================
        # DIBUJADO EN PANTALLA
        # ============================================================
        ventana.blit(fondo, (0, 0))

        pygame.draw.rect(ventana,COLOR_PALETA, PALETA)
        pygame.draw.ellipse(ventana, COLOR_PALETA, pelota)

        for bloque in bloques:
            ventana.blit(bloque["img"], bloque["rect"])

        puntuacion_texto = FUENTE.render(f"{puntuacion_jugador}", False, COLOR_PALETA)
        ventana.blit(puntuacion_texto, (50,50))

        vidas_texto = FUENTE.render(f"{vidas_disponibles}", False, COLOR_PALETA)
        ventana.blit(vidas_texto, (500,50))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()
