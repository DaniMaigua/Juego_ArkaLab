import pygame
import random

pygame.init

TODOS_LOS_POWERUPS = ["H", "C", "O", "Na", "Fe", "Ti", "He", "Ne"] # Lista con todos los powerups


def obtener_powerup_por_nivel(nivel_actual):
    cantidad = min(4 + (nivel_actual -1) * 2, 8) # Esta funcion nos dice cuantos powerups tenemos diponibles por nivel (min 4, max 8)
    return [None] + TODOS_LOS_POWERUPS[:cantidad]


def elegir_powerup(nivel_actual): #Funcion para appendear en la creacion de bloques
    powerups = obtener_powerup_por_nivel(nivel_actual) # Esta funcion toma cuantos powerups tenemos disponibles, y de ahi sortea cuales ingresar en los bloques de ese nivel
    return random.choice(powerups)




def aplicar_powerups(bloque, PALETA, velocidad_pelota_x, velocidad_pelota_y, color_pelota): #aplica efectos sobre pelota, paleta, colores, tamaños, velocidades
    if bloque == "H":
        velocidad_pelota_x *= -1.5 #Aumenta un poco la velocidad de la pelota
        velocidad_pelota_y *= -1.5
        color_pelota["valor"] = (255, 255, 0) # Cambia a color amarillo 
        print("Hidrogeno! Pelota mas liviana!")

    elif bloque == "C":
        PALETA.width = max(int(PALETA.width * 1.5), 30) # Agranda la paleta pero nunca a menos de 20 px
        velocidad_pelota_x *= 0.5 # Reduce un poco la velocidad de la pelota
        velocidad_pelota_y *= 0.5
        color_pelota["valor"] = (64, 64, 64) # Cambia a color gris
        print("Carbono! pelota mas pesada, y paleta mas grande!")

    elif bloque == "Na":
        PALETA.width = max(int(PALETA.width * 0.5), 20) # Achica la paleta pero nunca a menos de 20 px
        color_pelota["valor"] = (0, 255, 0)   # Cambia a color verde
        print("Hierro! activaste superfueza, y la paleta se achica!")

    elif bloque == "O":
        velocidad_pelota_y = max(1, velocidad_pelota_y // 2) # La pelota tiende a flotar mas sobre el eje Y
        color_pelota["valor"] = (0, 0, 255) # Pelota azul
        print("Oxigeno! pelota flotante!")

    elif bloque == "Fe":    
        color_pelota["valor"] = (0, 100, 255)
        PALETA.height = max(int(PALETA.height * 0.5), 10)  # Achicamos el Alto de la paleta
        print("Hierro! Paleta reduce su tamaño!")


    elif bloque == "Ti":
        velocidad_pelota_x *= 1
        velocidad_pelota_y *= 1
        color_pelota["valor"] = (135, 206, 235)
        print("Titanio! Pelota con mas fuerza")

    elif bloque == "He":
        velocidad_pelota_y *= max(1, velocidad_pelota_y // 2)
        color_pelota["valor"] = (255, 100, 255)
        print("Helio! pelota flotante")      

    elif bloque == "Ne":
        velocidad_pelota_x *= -0.8
        velocidad_pelota_y *= -0.8
        color_pelota["valor"] = (57, 255, 20)
        print("Neon! pelota brillante!")       


    return velocidad_pelota_x, velocidad_pelota_y