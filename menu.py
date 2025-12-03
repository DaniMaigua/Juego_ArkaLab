import pygame

from config import *
from juego import iniciar_juego
from ranking import mostrar_ranking
from creditos import mostrar_creditos


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets/Sonidos/sonido_inicio.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.3)
    

VENTANA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("ARKALAB - Menú del Juego")

nombre_icono = pygame.image.load('Assets/Intro/nombre_icono-37.png')
pygame.display.set_icon(nombre_icono)

fondo_menu = pygame.image.load("Assets/Fondo/Fondo_intro.png").convert_alpha()

logo = pygame.image.load("Assets/Intro/nombre_logo-38.png").convert_alpha()
logo_scale = pygame.transform.scale(logo, (430, 120))
eslogan = pygame.image.load("Assets/Intro/nombre_eslogan-39-39.png").convert_alpha()
eslogan_scale = pygame.transform.scale(eslogan, (200, 30))

# Cargar sonido
sonido_tecla_intro = pygame.mixer.Sound("Assets/Sonidos/sonido_vida.mp3")

imagenes_botones= {
"img_jugar": pygame.image.load("Assets/Intro/Botones/boton_jugar-27.png").convert_alpha(),
"img_ranking": pygame.image.load("Assets/Intro/Botones/boton_ranking-31.png").convert_alpha(), #CONVERT ALPHA respeta fondo transparente
"img_creditos": pygame.image.load("Assets/Intro/Botones/boton_creditos-32.png").convert_alpha(),
"img_salir": pygame.image.load("Assets/Intro/Botones/boton_salir-33.png").convert_alpha(),
"img_intro": pygame.image.load("Assets/Intro/Botones/boton_intro-34.png").convert_alpha(),
"img_omitir": pygame.image.load("Assets/Intro/Botones/boton_omitir-35.png").convert_alpha()}


imagenes_botones_inicio = {
    key: pygame.transform.scale(img, (180, 50))
    for key, img in imagenes_botones.items()
}


# Botones: texto, rectángulo, y estado de hover previo (para controlar el sonido)
botones = [
    {"imagen": imagenes_botones_inicio ["img_jugar"],
    "rect": pygame.Rect(300, 350, 120, 20),
    "tecla_intro": False, 
    "accion": "Jugar"},

    {"imagen": imagenes_botones_inicio ["img_ranking"], 
    "rect": pygame.Rect(300, 415, 120, 20),
    "tecla_intro": False, 
    "accion": "Ranking"},

    {"imagen": imagenes_botones_inicio ["img_creditos"], 
    "rect": pygame.Rect(300, 480, 120, 20),
    "tecla_intro": False, 
    "accion": "Créditos"},

    {"imagen": imagenes_botones_inicio ["img_salir"], 
    "rect": pygame.Rect(300, 545, 120, 20),
    "tecla_intro": False, 
    "accion": "Salir"}
]


corriendo = True


def dibujar_menu():

    VENTANA.blit(fondo_menu, (0, 0))
    VENTANA.blit(logo_scale, (150, 150))
    VENTANA.blit(eslogan_scale, (260, 280))
    mouse_pos = pygame.mouse.get_pos()

    for boton in botones:
        rect = boton["rect"]

        # Detectar si el mouse está sobre el botón
        if rect.collidepoint(mouse_pos):
            if not boton["tecla_intro"]:
                sonido_tecla_intro.play()
                boton["tecla_intro"] = True
        else:
            boton["tecla_intro"] = False

        
        img = boton["imagen"]
        #Crea un rectángulo del tamaño de la imagen y la centra en el botón.
        img_rect = boton["imagen"].get_rect(center=rect.center)

        VENTANA.blit(img,img_rect)
        
    pygame.display.update()

while corriendo:
    dibujar_menu()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for boton in botones:
                if boton["rect"].collidepoint(pos):
                    if boton["accion"] == "Jugar":
                        print("Iniciando el juego...")
                        corriendo = False        
                        iniciar_juego()          
                    elif boton["accion"] == "Ranking":
                        print("Mostrando el ranking...")
                        corriendo = False
                        mostrar_ranking(VENTANA, ANCHO, ALTO)
                    elif boton["accion"] == "Créditos":
                        print("Mostrando los créditos...")
                        corriendo = False
                        mostrar_creditos()
                    elif boton["accion"] == "Salir":
                        corriendo = False

pygame.quit()
