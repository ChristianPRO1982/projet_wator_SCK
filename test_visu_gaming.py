import pygame
#import imageio

#Initialisation de pygame
pygame.init()

#Charger le GIF avec imageio
gif_path = 'requin.gif'  # Remplacez ceci par le chemin de votre fichier GIF
#gif = imageio.mimread(gif_path)
#frames = [pygame.surfarray.make_surface(frame) for frame in gif]
giff = pygame.image.load(gif_path)

#Récupérer la taille du GIF
width, height = 800, 600

#Créer la fenêtre Pygame
screen = pygame.display.set_mode((width, height))

#Définir une horloge pour contrôler la vitesse d'affichage du GIF
clock = pygame.time.Clock()

background_color = (255,255,255)

running = True
#Boucle d'affichage du GIF
while running:
    screen.fill(background_color)# on efface tout avec cette couleur

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Afficher chaque image du GIF à l'écran
    for i in range(0,100,10):
        # screen.blit(frames[frame_index], (i, i+j))
        screen.blit(giff, (i, i+j))
        # frame_index = (frame_index + 1) % len(frames)

    pygame.display.flip()

    # Contrôler la vitesse d'affichage
    clock.tick(1)  # 30 images par seconde
    j+=10

Quitter Pygame
pygame.quit()