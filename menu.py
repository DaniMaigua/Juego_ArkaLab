import pygame

from constantes import *
from juego import iniciar_juego

# import bloques

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ALTO, ANCHO))
pygame.display.set_caption("Menú del Juego")


# Fuente
fuente = pygame.font.Font(None,20)


# Cargar sonido
sonido_hover = pygame.mixer.Sound("Assets/Sonidos/hover.mp3")
# img_jugar = pygame.image.load("Assets/Intro/Botones/boton_jugar-03.png").convert()
img_original = pygame.image.load("Assets/Intro/Botones/boton_jugar-03.png").convert_alpha()
img_jugar = pygame.transform.scale(img_original, (200, 60))



# Botones: texto, rectángulo, y estado de hover previo (para controlar el sonido)
botones = [
    {"imagen": img_jugar, 
     "rect": pygame.Rect(260, 150, 200, 60),
     "hover": False, 
     "accion": "Jugar"},

     {"imagen": img_jugar, 
     "rect": pygame.Rect(260, 150, 200, 60),
     "hover": False, 
     "accion": "Ranking"},

     {"imagen": img_jugar, 
     "rect": pygame.Rect(260, 150, 200, 60),
     "hover": False, 
     "accion": "Créditos"},

     {"imagen": img_jugar, 
     "rect": pygame.Rect(260, 150, 200, 60),
     "hover": False, 
     "accion": "Salir"}
]

# pygame.transform.scale(img,(ANCHO_BLOQUE, ALTO_BLOQUE))

# botones = [
#     {"texto": "Jugar", "rect": pygame.Rect(300, 150, 200, 60), "hover": False},
#     {"texto": "Ranking", "rect": pygame.Rect(300, 230, 200, 60), "hover": False},
#     {"texto": "Créditos", "rect": pygame.Rect(300, 310, 200, 60), "hover": False},
#     {"texto": "Salir", "rect": pygame.Rect(300, 390, 200, 60), "hover": False}
# ]

corriendo = True

def dibujar_menu():
    ventana.fill(AZUL_MARINO)
    mouse_pos = pygame.mouse.get_pos()

    for boton in botones:
        rect = boton["rect"]

        # Detectar si el mouse está sobre el botón
        if rect.collidepoint(mouse_pos):
            if not boton["hover"]:
                sonido_hover.play()
                boton["hover"] = True
            # color = AZUL_CLARO
        else:
            boton["hover"] = False
            # color = AZUL

        # pygame.draw.rect(ventana, color, rect)

        # texto = fuente.render(boton["texto"], True, AZUL_MARINO)
        img = boton["imagen"]
        #Crea un rectángulo del tamaño de la imagen y la centra en el botón.
        img_rect = boton["imagen"].get_rect(center=rect.center)
        # ventana.blit(texto,img_rect)
        ventana.blit(img,img_rect)
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
                        from juego import iniciar_juego
                        iniciar_juego()
                    elif boton["accion"] == "Ranking":
                        print("Mostrando el ranking...")
                    elif boton["accion"] == "Créditos":
                        print("Mostrando los créditos...")
                    elif boton["accion"] == "Salir":
                        corriendo = False

pygame.quit()