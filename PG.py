import pygame
pygame.init()

gif_eau = pygame.image.load('eau.png')
gif_poisson = pygame.image.load('poisson.png')
gif_requin = pygame.image.load('requin.png')

#Récupérer la taille du GIF
width, height = 800, 600

#Créer la fenêtre Pygame
screen = pygame.display.set_mode((width, height))

#Définir une horloge pour contrôler la vitesse d'affichage du GIF
clock = pygame.time.Clock()

background_color = (255,255,255)

def execution (monde):
    for ligne in monde.tableau_monde:
        pass