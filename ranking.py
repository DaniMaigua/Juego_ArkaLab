import pygame
import json
import os
from config import *


#ranking
def cargar_ranking():
    if not os.path.exists(RUTA_RANKING_TXT):
        return []
    with open(RUTA_RANKING_TXT, "r") as f:
        return json.loads(f.read() or "[]")

def guardar_puntaje(nombre, puntaje):
    ranking = cargar_ranking()
    ranking.append({"nombre": nombre, "puntaje": puntaje})
    with open(RUTA_RANKING_TXT, "w") as f:
        json.dump(ranking, f, indent=4)


def ordenar_descendente(ranking):
    """
    Ordena el ranking de mayor a menor puntaje usando el método burbuja.
    
    Cómo funciona:
    1. Recorre la lista múltiples veces
    2. En cada pasada, compara elementos adyacentes
    3. Si el elemento actual es menor que el siguiente, los intercambia
    4. Repite hasta que no haya más intercambios necesarios
    """
    n = len(ranking)
    
    # Recorrer todos los elementos
    for i in range(n):
        # Flag para optimizar (si no hay intercambios, ya está ordenado)
        hubo_intercambio = False
        
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Comparar puntajes: si el actual es MENOR que el siguiente, intercambiar
            # (queremos orden descendente: mayor a menor)
            if ranking[j]["puntaje"] < ranking[j + 1]["puntaje"]:
                # Intercambiar elementos
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]
                hubo_intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            break
    
    return ranking



def mostrar_ranking(ventana, ancho, alto):

    FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 40)
    FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-SemiBold.ttf", 25)
    
    # Cargar ranking y ordenar con método burbuja
    ranking = cargar_ranking()
    ranking = ordenar_descendente(ranking)  # AQUÍ SE USA BURBUJA
    ranking = ranking[:5]  # Top 5

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return True
        
        
        FONDO_CREDITOS = pygame.image.load("Assets/Fondo/Fondo_intro_opaco.png").convert_alpha()
        ventana.blit(FONDO_CREDITOS, (0, 0))
        pygame.display.set_caption("ARKALAB - Ranking")
        ventana.blit(FUENTE_TITULO.render("TOP 5 RANKING", True, AMARILLO), (ancho//2 - 140, 150))
        
        y = 220
        for i, j in enumerate(ranking, 1):
            ventana.blit(FUENTE_TEXTO.render(f"{i}. {j['nombre']} - {j['puntaje']}", True, BLANCO), (ancho//2 - 150, y))
            y += 60
        
        if not ranking:
            ventana.blit(FUENTE_TEXTO.render("No hay puntajes", True, BLANCO), (ancho//2 - 100, 200))
    
        ventana.blit(FUENTE_TEXTO.render("ESC para salir", True, AMARILLO), (ancho//2 - 80, alto - 230))

        pygame.display.flip()


def pedir_nombre(ventana, ancho, puntaje):
    FUENTE_TITULO = pygame.font.Font("Assets/Fuente/BungeeInline-Regular.ttf", 40)
    FUENTE_TEXTO = pygame.font.Font("Assets/Fuente/Oswald-SemiBold.ttf", 25)
    nombre = ""
    
    reloj = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre:
                    guardar_puntaje(nombre, puntaje)
                    return nombre
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 15 and evento.unicode.isprintable():
                    nombre += evento.unicode


        # Dibujar la pantalla
        FONDO_PUNTAJE = pygame.image.load("Assets/Fondo/fondo_puntaje.png").convert_alpha()
        ventana.blit(FONDO_PUNTAJE, (0, 0))

        # Título
        ventana.blit(FUENTE_TITULO.render("NUEVO PUNTAJE", True, AMARILLO), (ancho//2 - 200, 100))

        # Mostrar puntaje
        ventana.blit(FUENTE_TEXTO.render(f"Puntaje: {puntaje}", True, AMARILLO), (ancho//2 - 60, 200))
        
        # Instrucción
        ventana.blit(FUENTE_TEXTO.render("Ingresa tu nombre:", True, BLANCO), (ancho//2 - 80, 250))

        # Cuadro de texto con el nombre
        pygame.draw.rect(ventana, BLANCO, (ancho//2 - 200, 320, 400, 60), 3)
        texto_nombre = FUENTE_TEXTO.render(nombre + "|", True, BLANCO)
        ventana.blit(texto_nombre, (ancho//2 - 120, 330))

        ventana.blit(FUENTE_TEXTO.render("ENTER = Guardar", True, AMARILLO), (ancho//2 - 80, 700))
        pygame.display.flip()
        reloj.tick(60)