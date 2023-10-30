import os
import time
import initialisation
import monde
from poisson import Poisson
from requin import Requin

# récupération des variables d'initialisation
largeur_monde = int(initialisation.largeur_monde)
hauteur_monde = int(initialisation.hauteur_monde)
temps_reproduction_poisson = int(initialisation.temps_reproduction_poisson)
temps_reproduction_requin = int(initialisation.temps_reproduction_requin)
temps_energie_requin = int(initialisation.temps_energie_requin)
chronon = int(initialisation.chronon)
nb_poissons_init = int(initialisation.nb_poissons_init)
nb_requins_init = int(initialisation.nb_requins_init)
energie = 3

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
tour = 1
while tour <= chronon:
    time.sleep(0.3)
    os.system("clear")

    # à chaque tour de la simulation, MAIN appelle tous les ANIMAUX pour appliquer les règles du jeu
    for animal in monde.liste_animaux:
        # le MONDE vérifie l'état de cases voisine à l'ANIMAL sélectionné
        liste_de_choix = monde.liste_de_choix(animal.position)

        # l'ANIMAL se déplace
        ancienne_position, nouvelle_position, bebe,manger = animal.se_deplacer(liste_de_choix, largeur_monde, hauteur_monde)
        
        # l'ANIMAL indique au MONDE  ses actions
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

    print(monde, tour, "/", chronon)
    tour += 1