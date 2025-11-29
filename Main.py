# # # constante nombre de la ventana
# # NOMBRE_JUEGO = "Chucky: el programador de malbolge" 

# # # constante icono de la ventana
# # # ICONO = pygame.image.load("logo.png") 

# # # de este modo inicializamos pygame
# # pygame.init()

# # # creamos la ventana
# # # sin toda la logica de abajo se abrira y se cerrara rapidamente
# # ventana = pygame.display.set_mode((ANCHO, ALTO))
# # # ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN) # para pantalla completa
# # # ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE) # para pantalla redimensionable
# # # ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.NOFRAME) # para pantalla sin bordes


# # # Establecer el ícono de la ventana
# # pygame.display.set_caption(NOMBRE_JUEGO)

# # # Establecer el ícono de la ventana
# # # pygame.display.set_icon(ICONO)


# # # logica para mantener la ventana del juego siempre corriendo
# # corriendo = True

# # while corriendo:
    
# #     # realizaremos un for para recorrer los eventos
# #     for evento in pygame.event.get():
# #         # print(pygame.event.get())
# #         if evento.type == pygame.QUIT:
# #             corriendo = False
        
        
# #         pygame.display.update()

# # pygame.quit()

# #--------------------------------------------------------------------------------------------------------------------
# import pygame # importamos la libreria. Primero la debemos instalar



# import random
# import os

# from Main_intro import *
# from power_ups import aplicar_powerups

# # from bloques import pared_bloques

# # de este modo inicializamos pygame
# pygame.init()


# # creamos la ventana
# ANCHO, ALTO = 700, 750 # constantes del tamaño de la ventana

# # sin toda la logica de abajo se abrira y se cerrara rapidamente
# ventana = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("ArkaLab") # constante nombre de la ventana

# fondo = pygame.image.load("Assets/Fondo/fondo_nivel1 - copia.png").convert()

# puntuacion_jugador = 0

# # =================================================================================
# # PARED BLOQUES
# # =================================================================================

# RUTA_IMAGENES = "Assets/Elementos"  # carpeta donde tenés bloque1.png y bloque2.png

# imagenes_bloques = [
#     pygame.image.load(os.path.join(RUTA_IMAGENES, "bloque1_sodio.png")),
#     pygame.image.load(os.path.join(RUTA_IMAGENES, "bloque2_hidrogeno.png"))
# ]

# # Escalamos las imágenes al tamaño del bloque
# ANCHO_BLOQUE = 60
# ALTO_BLOQUE = 60

# imagenes_bloques = [
#     pygame.transform.scale(img, (ANCHO_BLOQUE, ALTO_BLOQUE))
#     for img in imagenes_bloques
# ]

# COLUMNAS = 8
# FILAS = 5
# ESPACIO = 7

# bloques = []
# # powerups = []

# def crear_bloques():
#     bloques.clear()

#     # ancho_grilla = COLUMNAS * (ANCHO_BLOQUE + ESPACIO) - ESPACIO

#     ancho_grilla = COLUMNAS * (ANCHO_BLOQUE + ESPACIO) - ESPACIO
#     offset_x = (ANCHO - ancho_grilla) // 2
#     offset_y = 150  # BAJAR LOS BLOQUES

#     for fila in range(FILAS):
#         for col in range(COLUMNAS):
#             x = offset_x + col * (ANCHO_BLOQUE + ESPACIO)
#             y = offset_y + fila * (ALTO_BLOQUE + ESPACIO)

#             rect = pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE)

#             # Imagen al azar (de las dos disponibles)
#             img = random.choice(imagenes_bloques)

#             bloques.append({
#                 "rect": rect,
#                 "img": img,
#                 "powerup": random.choice([None, "H", "C", "O", "Na"])
#             })
#             # powerup = sumamos la condicion que al azar    
#             # bloque = pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE)
#             # bloques.append(bloque)

#     # for fila in range(FILAS):
#     #     for col in range(COLUMNAS):
#     #         x = col * (ANCHO_BLOQUE + ESPACIO) + 20
#     #         y = fila * (ALTO_BLOQUE + ESPACIO) + 50
#     #         bloque = pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE)
#     #         bloques.append(bloque)

# crear_bloques()


# # #creacion pared de bloques
# # ALTURA_BLOQUE, ANCHO_BLOQUE = (50,50)
# # bloque = pygame.Rect((ANCHO - 100), (ALTO - 650), ALTURA_BLOQUE, ANCHO_BLOQUE)
# # # pared_bloques = [[bloque] * 6][[bloque] * 4]

# # pared_bloques = bloque

# # =================================================================================
# # PALETA
# # =================================================================================

# #definicion de forma de la paleta (es un rectangulo en este caso)
# PALETA = pygame.Rect(100, 650, 120, 25)
# VELOCIDAD_PALETA = 5
# COLOR_PALETA = (100, 100, 200)

# # =================================================================================
# # PELOTA
# # =================================================================================

# # PRIMERO definimos caracteristicas de la pelota
# TAMANIO_PELOTA = 30
# pelota = pygame.Rect((ANCHO // 3) - (TAMANIO_PELOTA // 2), (ALTO // 2) - (TAMANIO_PELOTA //2), TAMANIO_PELOTA, TAMANIO_PELOTA)
# color_pelota = {"valor": (100, 100, 200)}

# #ejes de movimiento de la pelota
# velocidad_pelota_x = 5 * random.choice([1, -1]) #ESTE VALOR RANDOM = puede quedar en 5 o - 5
# velocidad_pelota_y = 5 * random.choice([1, -1])


# # =================================================================================
# # PANTALLA
# # =================================================================================

# fuente = pygame.font.Font(None, 50)

# corriendo = True
# while corriendo:

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT: #APRETAR LA X
#             corriendo = False

# #se supone remplaza lo de arriba, ya que tiene en cuenta el movimiento de teclas
#     keys = pygame.key.get_pressed()

#     if keys[pygame.K_d] and PALETA.right < ANCHO:
#         PALETA.x += VELOCIDAD_PALETA
#     if keys[pygame.K_RIGHT] and PALETA.right < ANCHO:
#         PALETA.x += VELOCIDAD_PALETA 
#     if keys[pygame.K_a] and PALETA.left > 0:
#         PALETA.x -= VELOCIDAD_PALETA
#     if keys[pygame.K_LEFT] and PALETA.left > 0:
#         PALETA.x -= VELOCIDAD_PALETA

#     pelota.x += velocidad_pelota_x
#     pelota.y += velocidad_pelota_y

#     if pelota.top <= 0:
#         velocidad_pelota_y *= -1 #indica, si la pelota toca el top, que invierta el signo, de positivo a negativo
#     if pelota.left <= 0 or pelota.right >= ANCHO: 
#         velocidad_pelota_x *= - 1 #SOLO EN EJE X
    
#     #con estas coordenadas agregamos el movimiento
#     # PALETA.x += VELOCIDAD_PALETA
#     # print(VELOCIDAD_PALETA)

#     # COLISIONES
#     if pelota.colliderect(PALETA):
#         velocidad_pelota_y *= -1
#                                     #velocidad_pelota_x *= -1 #-> ver como funciona

#     #CONTEO DE PUNTOS
#     if pelota.bottom >= ALTO:
#         pelota.x, pelota.y = ((ANCHO //2) - (TAMANIO_PELOTA //2), (ALTO //2) - (TAMANIO_PELOTA //2))
#         velocidad_pelota_x *= random.choice([1, -1]) #esto esta repetitivo/ deberiamos ponerlo en funciones/ esto hace que vuelva a salir de manera random, no del mismo lado

#     # if PALETA.x + 50 > ANCHO or PALETA.x < 0:
#     #     VELOCIDAD_PALETA = -VELOCIDAD_PALETA

#     # --------------------------
#     # COLISIONES CON BLOQUES
#     # --------------------------
#     # PONER ESTE CICLO EN UNA FUNCION
#     # UTILIZAR ESTE CICLO PARA DETERMINAR DIVERSAS FUNCIONES DE LA PARED DE BLOQUES
#     #DISTINGUIR BLOQUES Y SU DISTRIBUCION
#     # for bloque in bloques[:]:  # copia de la lista para eliminar seguro
#     #     if pelota.colliderect(bloque):
#     #         bloques.remove(bloque)
#     #         velocidad_pelota_y *= -1
#     #         puntuacion_jugador += 5
#     #         break
#     # --------------------------
#     # COLISIONES CON BLOQUES
#     # --------------------------
    
#     def colisionar_pelota_bloque(bloques):
#         global velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador
#         for bloque in bloques[:]:
#             if pelota.colliderect(bloque["rect"]):
#                 bloques.remove(bloque)
#                 if bloque["powerup"] is not None:
#                     aplicar_powerups(bloque["powerup"], PALETA, velocidad_pelota_x, velocidad_pelota_y, color_pelota)  #Activa el powerup aleatoriamente al colisionar
#                 if abs(pelota.bottom -bloque["rect"].top) < 10 and velocidad_pelota_y > 0:
#                     velocidad_pelota_y *= -1
#                 elif abs(pelota.top -bloque["rect"].bottom) < 10 and velocidad_pelota_y < 0:    # funcion Abs para que rebote mas dinamicamente
#                     velocidad_pelota_y *= -1
#                 elif abs(pelota.right - bloque["rect"].left) < 10 and velocidad_pelota_x > 0:
#                     velocidad_pelota_x *= -1
#                 elif abs(pelota.left - bloque["rect"].right) < 10 and velocidad_pelota_x < 0:
#                     velocidad_pelota_x *= -1
#                 else:
#                     velocidad_pelota_x *= -1    #En caso de que no se pueda detectar cual es el punto de colision, vuelve en sentido contrario
#                     velocidad_pelota_y *= -1

#                 global puntuacion_jugador
#                 puntuacion_jugador += 5
#                 break



   

#     colisionar_pelota_bloque(bloques)
#    # actualizar_powerups(ventana, powerups, PALETA, velocidad_pelota_x, velocidad_pelota_y)
             

#     # --------------------------
#     # FONDO DE PANTALLA
#     # --------------------------

#     ventana.blit(fondo, (0, 0))
#     # ventana.fill((0, 0, 0))
#     #creacion del rectangulo (ubicacion, color, objeto -> un rectangulo)
#     pygame.draw.rect(ventana,COLOR_PALETA, PALETA)
#     pygame.draw.rect(ventana, (0, 0, 0), PALETA, 1) # Borde de la paleta
#     #LUEGO dibujamos la pelota
#     pygame.draw.ellipse(ventana, color_pelota["valor"], pelota)
#     pygame.draw.ellipse(ventana, (0, 0, 0), pelota, 1) # Borde de la pelota
#     # Dibujar bloques
#     # for bloque in bloques:
#     #     pygame.draw.rect(ventana, (200, 60, 60), bloque)
#     for bloque in bloques:
#         ventana.blit(bloque["img"], bloque["rect"])

# #DIBUJAMOS BLOQUES POR COLOR
#     # for bloque in bloques:
#     #     color = (200, 60, 60) if bloque["vida"] == 2 else (230, 220, 0)
#     #     pygame.draw.rect(ventana, color, bloque["rect"])


#     puntuacion_texto = fuente.render(f"{puntuacion_jugador}", False, COLOR_PALETA)

#     ventana.blit(puntuacion_texto, (50,50)) #lo bliteamos, osea pegamos el texto


# # # se va actualizando la pantalla
# # pygame.display.update() --> verificar porque no lo usamos

#     #Actualiza constantemente la pantalla
#     pygame.display.flip()

#     #RESTRICCION DE FPS
#     pygame.time.Clock().tick(60)
    

# pygame.quit()

