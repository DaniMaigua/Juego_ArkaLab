import pygame
# constantes del tamaño de la ventana
ANCHO = 700
ALTO = 750

#colores
AMARILLO = (255, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)
    
# constante nombre de la ventana
NOMBRE_JUEGO = "ArkaLab"

# constante icono de la ventana
ICONO = pygame.image.load("Assets/Intro/nombre_logo-38.png")

# constantes personaje
ANCHO_PERSONAJE = 50
ALTO_PERSONAJE = 50
COLOR_PERSONAJE = (255, 255, 0)


# carpeta donde estan los bloques elementos
RUTA_IMAGENES_ELEMENTOS = "Assets/Elementos"  

RUTA_RANKING_TXT = "Assets/Ranking/puntaje.txt"

# contantes de tamaño de bloque
ANCHO_BLOQUE = 60
ALTO_BLOQUE = 60

# contantes de tamaño matriz de bloque
COLUMNAS = 8
FILAS = 5
ESPACIO = 7

# constante de tamaño de palera
ALTO_PALETA = 25
LARGO_PALETA = 120
# PALETA = pygame.Rect(100, 650, LARGO_PALETA, ALTO) -> NICO TIENE 100 YO 290 ver
PALETA = pygame.Rect(290, 680, LARGO_PALETA, 25)
VELOCIDAD_PALETA = 15

# constante colores
COLOR_PALETA = (100, 100, 200)
AZUL_MARINO = (0, 0, 128)


# PRIMERO definimos caracteristicas de la pelota
TAMANIO_PELOTA = 30

FUENTE = None
FUENTE_TITULO = None
FUENTE_TEXTO = None

# FUENTE = pygame.font.Font(None, 50)
# FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 70)
# # FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-Bold.ttf", 30)


# VARIABLES DEL JUEGO
velocidad_pelota_x = 5
velocidad_pelota_y = -5
puntuacion_jugador = 0
pelota_en_movimiento = False
vidas = 3




# vidas_iconos = [
# {"vida1":  pygame.image.load("") },
# {"vida2": },
# {"vida3": }
# ]
# # FUENTE = pygame.font.Font(None, 50)
# FUENTE = None
#ejes de movimiento de la pelota
# velocidad_pelota_x = 5 * random.choice([1, -1]) #ESTE VALOR RANDOM = puede quedar en 5 o - 5 -> version NICO VER  
pelota = pygame.Rect (PALETA.centerx - (TAMANIO_PELOTA // 2), PALETA.top - (TAMANIO_PELOTA + 5), TAMANIO_PELOTA, TAMANIO_PELOTA)
color_pelota = {"valor": (100, 100, 200)}

