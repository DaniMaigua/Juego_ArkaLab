import pygame

from constantes import ANCHO_PERSONAJE, ALTO_PERSONAJE, COLOR_PERSONAJE

class Personaje:
    
    def __init__(self, x=None, y=None):
        self.forma = pygame.Rect(0, 0, ANCHO_PERSONAJE, ALTO_PERSONAJE)
        if x is not None and y is not None:
            self.forma.center = (x, y)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, COLOR_PERSONAJE, self.forma)

#verificar si tiene sentido tener esta variante de personaje, ya que serà una pelota