import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 1000
hauteur_ecran = 1000

# Créez une fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

# Chargez l'image depuis un fichier (l'image est dans le même dossier que le script)
poisson_img = pygame.image.load("images/poisson2.jpg")
requin_img = pygame.image.load("images/requin_image.jpg")
eau_img = pygame.image.load("images/eau.jpg")

fenetre.fill((255, 255, 255))

def execution (monde):
    y_image = 0
    for ligne in monde.tableau_monde:
        x_image= 0
        for colonne in ligne:
            if str(colonne) == "P":
                image = poisson_img
            elif str(colonne)== "R":
                image = requin_img
            else:
                image = eau_img
            fenetre.blit(image, (x_image, y_image))  
            x_image=x_image+50
        y_image=y_image+50
    pygame.display.flip()
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
    return continuer

def execution_finale():
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
    pygame.quit()