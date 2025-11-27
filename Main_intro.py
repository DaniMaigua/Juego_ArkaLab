import pygame

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menú del Juego")

# Colores
AZUL_MARINO = (0, 0, 128)
AZUL = (0, 120, 215)
AZUL_CLARO = (100, 180, 255)

# Fuente
fuente = pygame.font.Font(None, 15)


# Cargar sonido
sonido_hover = pygame.mixer.Sound("hover.mp3")

# Botones: texto, rectángulo, y estado de hover previo (para controlar el sonido)
botones = [
    {"texto": "Jugar", "rect": pygame.Rect(300, 150, 200, 60), "hover": False},
    {"texto": "Ranking", "rect": pygame.Rect(300, 230, 200, 60), "hover": False},
    {"texto": "Créditos", "rect": pygame.Rect(300, 310, 200, 60), "hover": False},
    {"texto": "Salir", "rect": pygame.Rect(300, 390, 200, 60), "hover": False}
]

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
            color = AZUL_CLARO
        else:
            boton["hover"] = False
            color = AZUL

        pygame.draw.rect(ventana, color, rect)

        texto = fuente.render(boton["texto"], True, AZUL_MARINO)
        texto_rect = texto.get_rect(center=rect.center)
        ventana.blit(texto, texto_rect)

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
                    if boton["texto"] == "Jugar":
                        print("Iniciando el juego...")
                    elif boton["texto"] == "Ranking":
                        print("Mostrando el ranking...")
                    elif boton["texto"] == "Créditos":
                        print("Mostrando los créditos...")
                    elif boton["texto"] == "Salir":
                        corriendo = False

pygame.quit()