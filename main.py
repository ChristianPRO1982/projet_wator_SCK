import os
import time
import initialisation
import SQL
import monde
from poisson import Poisson
from requin import Requin

# récupération des variables d'initialisation
largeur_monde = int(initialisation.largeur_monde)
hauteur_monde = int(initialisation.hauteur_monde)
temps_reproduction_poisson = int(initialisation.temps_reproduction_poisson)
temps_reproduction_poisson_max = int(initialisation.temps_reproduction_poisson_max)
temps_reproduction_requin = int(initialisation.temps_reproduction_requin)
temps_reproduction_requin_max = int(initialisation.temps_reproduction_requin_max)
temps_energie_requin = int(initialisation.temps_energie_requin)
temps_energie_requin_max = int(initialisation.temps_energie_requin_max)
chronon = int(initialisation.chronon)
nb_poissons_init = int(initialisation.nb_poissons_init)
nb_poissons_init_max = int(initialisation.nb_poissons_init_max)
nb_requins_init = int(initialisation.nb_requins_init)
nb_requins_init_max = int(initialisation.nb_requins_init_max)
energie = 3 # énergie potentiel d'un poisson

# génération du monde vide
monde = monde.Monde(largeur_monde,
                    hauteur_monde,
                    temps_reproduction_poisson,
                    temps_reproduction_requin,
                    temps_energie_requin,
                    nb_poissons_init,
                    nb_requins_init)

# génération des poissons (initialisation)
for i in range(nb_poissons_init):
    nouveau_poisson = Poisson(monde.newID(), temps_reproduction_poisson, energie, monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_poisson, nouveau_poisson.position)

# génération des requins (initialisation)
for i in range(nb_requins_init):
    nouveau_requin = Requin(monde.newID(), temps_energie_requin, temps_reproduction_requin, monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_requin, nouveau_requin.position)

os.system("clear")
print(monde, "init")
etat_du_monde = [] # permet de sauvegarder l'état du monde à chaque chronon
tour = 1
while tour <= chronon:
    time.sleep(0.3)
    os.system("clear")

    # à chaque tour de la simulation, MAIN appelle tous les ANIMAUX pour appliquer les règles du jeu
    for animal in monde.liste_animaux:
        # le MONDE vérifie l'état de cases voisine à l'ANIMAL sélectionné
        liste_de_choix = monde.liste_de_choix(animal.position)

        # l'ANIMAL se déplace
        ancienne_position, nouvelle_position, bebe, manger = animal.se_deplacer(liste_de_choix, largeur_monde, hauteur_monde)
        

        ##########################################
        # l'ANIMAL indique au MONDE  ses actions #
        ##########################################

        # le requin perd 1 d'énergie
        if str(animal) == 'R':
            animal.baisse_energie()

        # l'ANIMAL mange un autre animal dans la nouvelle position
        if manger == True:
            animal.nourrir(monde.animal_mange(nouvelle_position))
            

        # l'ANIMAL se déplace
        if ancienne_position != nouvelle_position:
            monde.deplacer_animal(animal, ancienne_position, nouvelle_position)

        # cas d'une naissance
        if ancienne_position != nouvelle_position and bebe and monde.plein() < largeur_monde * hauteur_monde:
            if str(animal) == "P":
                # poisson
                nouvel_animal = Poisson(monde.newID(), temps_reproduction_poisson, energie, ancienne_position)
            else:
                # requin
                nouvel_animal = Requin(monde.newID(), temps_energie_requin, temps_reproduction_requin, ancienne_position)
            monde.ajout_animal(nouvel_animal, nouvel_animal.position)

        # cas où l'ANIMAL est arrivé à 0 d'énergie
        if animal.energie <= 0:
            monde.mort_animal(animal.ID)

    print(monde, tour, "/", chronon)
    etat_du_monde.append((tour, monde.nb_poisson, monde.nb_requin, largeur_monde * hauteur_monde - monde.nb_poisson - monde.nb_requin))
    tour += 1

# on ajoute la simulation en BDD
# SQL.new_simulation(monde, tour, chronon, largeur_monde * hauteur_monde - monde.nb_poisson - monde.nb_requin)
# SQL.new_simulation_evolution(etat_du_monde)