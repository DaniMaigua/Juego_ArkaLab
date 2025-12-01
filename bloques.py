import pygame
import random
from constantes import *
from power_ups import aplicar_powerups

# sonido_colision = pygame.mixer.Sound("Assets/Sonidos/sonido_colision_bloque2.mp3")
# sonido_colision.set_volume(0.5)  # opcional

# =================================================================================
# PARED BLOQUES
# =================================================================================


# Diccionario de bloques -> util para power ups
# imagenes_bloques = [
#  {"Na": pygame.image.load("Assets/Elementos/Celeste/celeste_alcalino_hidrogeno.png")} ,
#     # "H": pygame.image.load("Assets/Elementos/Celeste/celeste_alcalino_sodio.png"),
#     # "B": pygame.image.load("Assets/Elementos/Amarillo/amarillo_metaloide_boro-22.png"),
#     # "Si": pygame.image.load("Assets/Elementos/Amarillo/amarillo_metaloide_silicio-23.png"),
#     # "P": pygame.image.load("Assets/Elementos/Azul/azul_lantanido_fosforo-20.png"),
#     # "Th": pygame.image.load("Assets/Elementos/Naranja/naranja_actinido_torio-14.png"),
#     # "U": pygame.image.load("Assets/Elementos/Naranja/naranja_actinido_uranio-15.png"),
#     # "He": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_helio-17.png"),
#     # "Ne": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_neon-18.png"),
#     # "Kr": pygame.image.load("Assets/Elementos/Rosa/rosa_gas_noble_kripton-19.png"),
#     # "Ce": pygame.image.load("Assets/Elementos/Verde_Agua/verde_agua_nometal_cerio-16.png"),
#     # "Cr": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_cromo-11.png"),
#     # "Fe": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_hierro-12.png"),
#     # "Mt": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_meitnerio-13.png"),
#     # "Ti": pygame.image.load("Assets/Elementos/Violeta/violeta_metal_transicional_titanio-10.png"),
# ]


imagenes_bloques = {
    "Na": pygame.image.load("Assets/Elementos/Celeste/celeste_alcalino_hidrogeno.png") ,
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

#comentar filas y columnas constantes
bloques = []
# FUNCIÓN PARA CREAR LA MATRIZ DE BLOQUES
def crear_bloques(nivel_actual, columnas = 8, filas = 5):
    bloques.clear()

    # ancho_matriz_bloques = COLUMNAS * (ANCHO_BLOQUE + ESPACIO) - ESPACIO
    ancho_matriz_bloques = columnas * (ANCHO_BLOQUE + ESPACIO) - ESPACIO
    offset_x = (ANCHO - ancho_matriz_bloques) // 2 #centrarlo segun tamaño matriz
    offset_y = 150  # BAJAR LOS BLOQUES

    for fila in range(filas):
        for col in range(columnas):

            if nivel_actual == 1:
                x = offset_x + col * (ANCHO_BLOQUE + ESPACIO)
                y = offset_y + fila * (ALTO_BLOQUE + ESPACIO)

            elif nivel_actual == 2:           #el nivel 2 forma una piramide con los bloques
                if col <= fila:
                    x = offset_x + col * (ANCHO_BLOQUE + ESPACIO)
                    y = offset_y + fila * (ALTO_BLOQUE + ESPACIO)
                else:
                    continue

            elif nivel_actual == 3:           #el nivel 3 forma un bloque mas grande y con zig zag a los costados
                offset = (fila % 2) * (ANCHO_BLOQUE + ESPACIO)
                x = offset_x + col * (ANCHO_BLOQUE + ESPACIO) + offset
                y = offset_y + fila * (ANCHO_BLOQUE + ESPACIO)

            else:
                x = offset_x + col * (ANCHO_BLOQUE + ESPACIO)   #esto es para dejar uno por defecto
                y = offset_y + fila * (ALTO_BLOQUE + ESPACIO)  


            rect = pygame.Rect(x, y, ANCHO_BLOQUE, ALTO_BLOQUE)

            # Imagen al azar (de las disponibles)
            img = random.choice(imagenes_bloques)

            #DICCIONARIO -> rectangulo e imagen
            bloques.append({
            "rect": rect,
            "img": img,
            "powerup": random.choice([None, "H", "C", "O", "Na"]) 
            #falta sumar los nuevos powerups del nivel 2 y 3
        })
    fondo = pygame.image.load(f"Assets/Fondo/fondo_nivel{nivel_actual}.png")    
    #fondo ahora es una variable, recibe la ruta y cambia segun el nivel actual.
    return bloques, fondo
            


# FUNCIÓN PARA IDENTIFICAR COLISION DE PELOTAS Y ACTIVAR POWERUPS
def colisionar_pelota_bloque(bloques, velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador, pelota, color_pelota, fondo, nivel_actual):
    for bloque in bloques[:]:
        if pelota.colliderect(bloque["rect"]):
            sonido_colision = pygame.mixer.Sound("Assets/Sonidos/sonido_colision_bloque2.mp3")
            sonido_colision.set_volume(0.5)  # opcional
            sonido_colision.play()
            bloques.remove(bloque)
            # # pygame.init()
            # pygame.mixer.init()
            # pygame.mixer.music.load("Assets/Sonidos/sonido_colision_bloque2.mp3")
            # # pygame.mixer.music.play(loops=-1)
            # # pygame.mixer.music.set_volume(0.3)

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
        # if not bloques: #este IF es la condicion para pasar de nivel
        #     nivel_actual += 1
        #     bloques_list, fondo = crear_bloques(nivel_actual)
        #     break

    return bloques, velocidad_pelota_y, velocidad_pelota_x, puntuacion_jugador, pelota, color_pelota, fondo, nivel_actual
# retornamos todo porque sirve para alimentar nuevamente a la funcion colisionar con el nuevo nivel