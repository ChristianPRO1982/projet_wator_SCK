import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de l'écran
largeur_ecran = 1000
hauteur_ecran = 1000

# Créez une fenêtre Pygame
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

# Chargez l'image depuis un fichier (l'image est dans le même dossier que le script)
jour_poisson1_img = pygame.image.load("images/images/jour_poisson1.jpg")
jour_poisson2_img = pygame.image.load("images/images/jour_poisson2.jpg")
jour_poisson3_img = pygame.image.load("images/images/jour_poisson3.jpg")
jour_requin_img = pygame.image.load("images/images/jour_requin.jpg")
jour_requin_cannibale_img = pygame.image.load("images/images/jour_requin_cannibale.jpg")
jour_algue_img = pygame.image.load("images/images/jour_algue.jpg")
jour_rocher_img = pygame.image.load("images/images/jour_rocher.jpg")
jour_eau_img = pygame.image.load("images/images/jour_eau.jpg")
nuit_poisson1_img = pygame.image.load("images/images/nuit_poisson1.jpg")
nuit_poisson2_img = pygame.image.load("images/images/nuit_poisson2.jpg")
nuit_poisson3_img = pygame.image.load("images/images/nuit_poisson3.jpg")
nuit_requin_img = pygame.image.load("images/images/nuit_requin.jpg")
nuit_requin_cannibale_img = pygame.image.load("images/images/nuit_requin_cannibale.jpg")
nuit_algue_img = pygame.image.load("images/images/nuit_algue.jpg")
nuit_rocher_img = pygame.image.load("images/images/nuit_rocher.jpg")
nuit_eau_img = pygame.image.load("images/images/nuit_eau.jpg")

def execution (monde):

    # gestion du jour et de la nuit
    if monde.jour_nuit == 1:
        fenetre.fill((128, 222, 255))

        poisson1_img = jour_poisson1_img
        poisson2_img = jour_poisson2_img
        poisson3_img = jour_poisson3_img
        requin_img = jour_requin_img
        requin_cannibale_img = jour_requin_cannibale_img
        algue_img = jour_algue_img
        rocher_img = jour_rocher_img
        eau_img = jour_eau_img
    else:
        fenetre.fill((0, 50, 128))

        poisson1_img = nuit_poisson1_img
        poisson2_img = nuit_poisson2_img
        poisson3_img = nuit_poisson3_img
        requin_img = nuit_requin_img
        requin_cannibale_img = nuit_requin_cannibale_img
        algue_img = nuit_algue_img
        rocher_img = nuit_rocher_img
        eau_img = nuit_eau_img

    y_image = 0
    for ligne in monde.tableau_monde:
        x_image= 0
        for colonne in ligne:
            if str(colonne) == "P":
                if colonne.image == 'poisson1':
                    image = poisson1_img
                elif colonne.image == 'poisson2':
                    image = poisson2_img
                else:
                    image = poisson3_img
            elif str(colonne)== "R":
                if colonne.image == 'requin':
                    image = requin_img
                else:
                    image = requin_cannibale_img
            elif str(colonne)== "C":
                image = rocher_img
            elif str(colonne)== "A":
                image = algue_img
            else:
                image = eau_img
            fenetre.blit(image, (x_image, y_image))
            x_image = x_image + 50
        y_image = y_image + 50
    
    pygame.display.flip()
    
    continuer = True
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