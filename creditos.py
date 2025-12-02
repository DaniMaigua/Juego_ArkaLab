import pygame

from config import *

#creditos
def mostrar_creditos():

    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    FONDO_CREDITOS = pygame.image.load("Assets/Fondo/Fondo_intro_opaco.png").convert_alpha()
    VENTANA.blit(FONDO_CREDITOS, (0, 0))
    pygame.display.set_caption("ARKALAB - Creditos")

    FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 40)
    FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-SemiBold.ttf", 25)

    creditos = ["Segundo Parcial - Programación I (2025)", "Daniela Maigua", 
                "Nicolas Soplan", "Janeth Pinedo", "Docente: Enzo Zotti"]
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return True

        VENTANA.blit(FUENTE_TITULO.render("CREDITOS", True, AMARILLO), (ANCHO//2 - 140, 150))
        
        y = 220
        for linea in creditos:
            texto = FUENTE_TEXTO.render(linea, True, BLANCO)
            VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, y))
            y += 45
        
        VENTANA.blit(FUENTE_TEXTO.render("ESC para volver", True, AMARILLO), (ANCHO//2 - 80, ALTO - 230))
        pygame.display.flip()