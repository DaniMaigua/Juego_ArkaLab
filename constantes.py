import pygame
# constantes del tamaño de la ventana
ANCHO = 700
ALTO = 750

# constante nombre de la ventana
NOMBRE_JUEGO = "ArkaLab"

# constante icono de la ventana
ICONO = pygame.image.load("assets/logo.png") 

# constantes personaje
ANCHO_PERSONAJE = 50
ALTO_PERSONAJE = 50
COLOR_PERSONAJE = (255, 255, 0)


# carpeta donde estan los bloques elementos
RUTA_IMAGENES_ELEMENTOS = "Assets/Elementos"  

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
# PALETA = pygame.Rect(100, 650, LARGO_PALETA, ALTO)
PALETA = pygame.Rect(290, 680, LARGO_PALETA, 25)
VELOCIDAD_PALETA = 6

# constante colores
COLOR_PALETA = (100, 100, 200)
AZUL_MARINO = (0, 0, 128)


# PRIMERO definimos caracteristicas de la pelota
TAMANIO_PELOTA = 30
