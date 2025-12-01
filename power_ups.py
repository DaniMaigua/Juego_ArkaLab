import pygame
import random

pygame.init

# Mueve, dibuja o aplica efectos si los toca la pelota

# def actualizar_powerups(ventana, powerups, PALETA, velocidad_pelota_x, velocidad_pelota_y):

#     for powerup in powerups[:]:

#         if powerup["tipo"] == "H":
#             color = (255, 255, 0)
#         elif powerup ["tipo"] == "C":
#             color = (0, 200, 0)
#         elif powerup ["tipo"] == "Na":
#             color =(255, 100, 100)    
#         else:
#             color = (255, 255, 255)    

#         pygame.draw.rect(ventana, color, powerup["rect"])
        
#         if PALETA.colliderect(powerup["rect"]):
#             aplicar_powerups(powerup, PALETA, velocidad_pelota_x, velocidad_pelota_y)
#             powerups.remove(powerup)

# # 


# POWERUPS_POR_NIVEL = {  
#     1: [None, "H", "C", "O", "Na"],
#     2: [None, "Fe", "Ti", "He", "Ne"],
#     3: [None, "Au", "Ag", "Pb", "Zn"],
# }

# def obtener_powerup(nivel_actual):
#     #Devuelve un powerup aleatorio según el nivel actual
#     powerups = POWERUPS_POR_NIVEL.get(nivel_actual, [None])
#     return random.choice(powerups)




def aplicar_powerups(tipo, PALETA, velocidad_pelota_x, velocidad_pelota_y, color_pelota):#nombre_imagen):

    if tipo == "H":
        velocidad_pelota_x *= 1.3 #Aumenta un poco la velocidad de la pelota
        velocidad_pelota_y *= 1.3
        color_pelota["valor"] = (255, 255, 0) # Cambia a color amarillo 

    elif tipo == "C":
        PALETA.width = max(int(PALETA.width * 1.5), 30) # Agranda la paleta pero nunca a menos de 20 px
        velocidad_pelota_x *= 0.5 # Reduce un poco la velocidad de la pelota
        velocidad_pelota_y *= 0.5
        color_pelota["valor"] = (64, 64, 64) # Cambia a color gris

    elif tipo == "Na":
        PALETA.width = max(int(PALETA.width * 0.5), 20) # Achica la paleta pero nunca a menos de 20 px
        color_pelota["valor"] = (0, 255, 0)   # Cambia a color verde

    return velocidad_pelota_x, velocidad_pelota_y
    


