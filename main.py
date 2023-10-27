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
    nouveau_poisson = Poisson(temps_reproduction_poisson, energie, monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_poisson, nouveau_poisson.position)

# génération des requins (initialisation)
for i in range(nb_requins_init):
    nouveau_requin = Requin(temps_energie_requin, temps_reproduction_requin, monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_requin, nouveau_requin.position)

tour = 0
while tour < chronon:
    time.sleep(0.5)
    os.system("clear")

    for animal in monde.liste_animaux:
        if animal.type == "poisson":
            ancienne_position, nouvelle_position, bebe = animal.se_deplacer(monde.liste_de_choix(animal.position), largeur_monde, hauteur_monde)
            if monde.deplacer_poisson(ancienne_position, nouvelle_position) and bebe:
                nouveau_poisson = Poisson(temps_reproduction_poisson, energie, ancienne_position)
                monde.ajout_animal(nouveau_poisson, nouveau_poisson.position)

    print(monde)
    tour += 1