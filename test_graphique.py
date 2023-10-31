import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 800
hauteur_ecran = 600

# Créez une fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

# Chargez l'image depuis un fichier (l'image est dans le même dossier que le script)
mon_image = pygame.image.load("poisson.jpg")
mon_image2 = pygame.image.load("requin.jpg")
mon_image3 = pygame.image.load("eau.jpg")



# Position de l'image
x_image = 0
y_image = 0

# Boucle principale de Pygame
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    # Effacez l'écran
    fenetre.fill((0, 0, 0))  # Fond blanc

    # Affichez l'image à la position spécifiée
    fenetre.blit(mon_image, (x_image, y_image))
    fenetre.blit(mon_image2, (x_image, y_image))
    fenetre.blit(mon_image3, (x_image, y_image))


    # Rafraîchissez l'écran
    pygame.display.flip()

# Quitte Pygame
pygame.quit()
