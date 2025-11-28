
import pygame # importamos la libreria. Primero la debemos instalar

import random
import os

# from menu import *
from constantes import *

# from bloques import pared_bloques

# de este modo inicializamos pygame
pygame.init()


def iniciar_juego():
    velocidad_pelota_x = 5
    velocidad_pelota_y = -5
    puntuacion_jugador = 0

    #IMPORTANTE: sin toda la logica de abajo se abrira y se cerrara rapidamente
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("ArkaLab") # constante nombre de la ventana

    fondo = pygame.image.load("Assets/Fondo/fondo_700_x_750_opaco.png").convert()


    # =================================================================================
    # PARED BLOQUES
    # =================================================================================


    imagenes_bloques = [
        pygame.image.load(os.path.join(RUTA_IMAGENES_ELEMENTOS, "bloque1_sodio.png")),
        pygame.image.load(os.path.join(RUTA_IMAGENES_ELEMENTOS, "bloque2_hidrogeno.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Amarillo" , "amarillo_metaloide_boro-22.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Amarillo" , "amarillo_metaloide_silicio-23.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Azul" , "azul_lantanido_fosforo-20.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Naranja" , "naranja_actinido_torio-14.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Naranja" , "naranja_actinido_uranio-15.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Rosa" , "rosa_gas_noble_helio-17.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Rosa" , "rosa_gas_noble_neon-18.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Rosa" , "rosa_gas_noble_kripton-19.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Verde_Agua" , "verde_agua_nometal_cerio-16.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Violeta" , "violeta_metal_transicional_cromo-11.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Violeta" , "violeta_metal_transicional_hierro-12.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Violeta" , "violeta_metal_transicional_meitnerio-13.png")),
        pygame.image.load(os.path.join("Assets/Elementos/Violeta" , "violeta_metal_transicional_titanio-10.png"))
    ]


    imagenes_bloques = [
        pygame.transform.scale(img,(ANCHO_BLOQUE, ALTO_BLOQUE))
        for img in imagenes_bloques
    ]


    bloques = []

    def crear_bloques():
        bloques.clear()

        ancho_matriz_bloques = COLUMNAS * (ANCHO_BLOQUE + ESPACIO) - ESPACIO
        offset_x = (ANCHO - ancho_matriz_bloques) // 2
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

    # # PRIMERO definimos caracteristicas de la pelota
    pelota = pygame.Rect((ANCHO // 3) - (TAMANIO_PELOTA // 2), (ALTO // 3) - (TAMANIO_PELOTA //2), TAMANIO_PELOTA, TAMANIO_PELOTA)

    #ejes de movimiento de la pelota
    velocidad_pelota_x = 5 * random.choice([1, -1]) #ESTE VALOR RANDOM = puede quedar en 5 o - 5
    velocidad_pelota_y = 5 * random.choice([1, -1])


    # =================================================================================
    # PANTALLA
    # =================================================================================

    fuente = pygame.font.Font(None, 50)

    corriendo = True

    #CONTEO DE VIDAS 
    vidas = 3
    while corriendo:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: #APRETAR LA X
                corriendo = False

    #se supone remplaza lo de arriba, ya que tiene en cuenta el movimiento de teclas
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and PALETA.right < ANCHO:
            PALETA.x += VELOCIDAD_PALETA
        if keys[pygame.K_a] and PALETA.left > 0:
            PALETA.x -= VELOCIDAD_PALETA

        #SEGUN EL EJE INDICADO, La pelota tomará velocidad
        pelota.x += velocidad_pelota_x #HACERLOS CONSTANTES
        pelota.y += velocidad_pelota_y


        if pelota.top <= 0:
            velocidad_pelota_y *= -1 #indica, si la pelota toca el top, que invierta el signo, de positivo a negativo. Como consecuencia, cambiará el sentido de direcciòn. 
        if pelota.left <= 0 or pelota.right >= ANCHO: 
            velocidad_pelota_x *= - 1 #SOLO EN EJE X, bordes laterales.
        
        #con estas coordenadas agregamos el movimiento
        # PALETA.x += VELOCIDAD_PALETA
        # print(VELOCIDAD_PALETA)

        # COLISIONES

        #EREBOTE GENERICO DE PELOTA CON PALETA
        if pelota.colliderect(PALETA):
            velocidad_pelota_y *= -1
            velocidad_pelota_x *= -1 #-> ver como funciona


        # PERDER VIDA
        if pelota.bottom >= ALTO:
            vidas -= 1

            # Reiniciar pelota
            pelota.x = (ANCHO // 2) - (TAMANIO_PELOTA // 2)
            pelota.y = (ALTO // 2) - (TAMANIO_PELOTA // 2)
            
            velocidad_pelota_x = 5 * random.choice([1, -1])
            velocidad_pelota_y = -5  # siempre hacia arriba

        if vidas <= 0:
            # Reiniciar juego completo
            vidas = 3
            puntuacion_jugador = 0
            crear_bloques()


        # --------------------------
        # COLISIONES CON BLOQUES
        # --------------------------
        # PONER ESTE CICLO EN UNA FUNCION
        # UTILIZAR ESTE CICLO PARA DETERMINAR DIVERSAS FUNCIONES DE LA PARED DE BLOQUES
        # DISTINGUIR BLOQUES Y SU DISTRIBUCION

        # --------------------------
        # COLISIONES CON BLOQUES
        # --------------------------
        
        def colisionar_pelota_bloque(bloques, velocidad_pelota_y, puntuacion_jugador):
            for bloque in bloques[:]:
                if pelota.colliderect(bloque["rect"]):
                    bloques.remove(bloque)
                    velocidad_pelota_y *= -1
                    puntuacion_jugador += 5
                    break
            return puntuacion_jugador
                
        colisionar_pelota_bloque(bloques, velocidad_pelota_y, puntuacion_jugador)
        # --------------------------
        # FONDO DE PANTALLA
        # --------------------------
        ventana.blit(fondo, (0, 0))

        #creacion del rectangulo PALETA (ubicacion, color, objeto -> un rectangulo)
        pygame.draw.rect(ventana,COLOR_PALETA, PALETA)
        #LUEGO dibujamos la pelota
        pygame.draw.ellipse(ventana, COLOR_PALETA, pelota)
        
        # Pegar imagen de bloques
        for bloque in bloques:
            ventana.blit(bloque["img"], bloque["rect"])

    #DIBUJAMOS BLOQUES POR COLOR
        # for bloque in bloques:
        #     color = (200, 60, 60) if bloque["vida"] == 2 else (230, 220, 0)
        #     pygame.draw.rect(ventana, color, bloque["rect"])

        # --------------------------
        # GAME OVER
        # --------------------------   
        puntuacion_vidas = fuente.render(f"Vidas: {vidas}", False, COLOR_PALETA)
        if vidas == 0:
            puntuacion_vidas = fuente.render("Game Over", False, COLOR_PALETA)
        ventana.blit(puntuacion_vidas, (500,50)) #lo bliteamos, osea pegamos el texto

        puntuacion_texto = fuente.render(f"{puntuacion_jugador}", False, COLOR_PALETA)
        ventana.blit(puntuacion_texto, (50,50)) #lo bliteamos, osea pegamos el texto



        # --------------------------
        # PUNTUACION TEXTO
        # --------------------------  
        puntuacion_texto = fuente.render(f"{puntuacion_jugador}", False, COLOR_PALETA)
        ventana.blit(puntuacion_texto, (50,50)) #lo bliteamos, osea pegamos el texto


    # # se va actualizando la pantalla
        # pygame.display.update() --> funcion parecida a .flip
        #  dos funciones  que actualizan la pantalla,  diferencias sutiles: flip() actualiza toda la superficie de la pantalla, mientras que update() puede actualizar toda la pantalla o un área específica si se le pasan parámetros.

        #Actualiza constantemente la pantalla
        pygame.display.flip() #PODRIA SER TAMBIEN UPDATE

        #RESTRICCION DE FPS
        pygame.time.Clock().tick(60)
        

    pygame.quit() #para liberar recursos -> VER

