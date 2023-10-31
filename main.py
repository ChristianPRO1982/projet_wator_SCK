import os
import time
import initialisation
import SQL
import monde as new_monde
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
nb_poissons_init = int(initialisation.nb_poissons_init)
nb_poissons_init_max = int(initialisation.nb_poissons_init_max)
nb_requins_init = int(initialisation.nb_requins_init)
nb_requins_init_max = int(initialisation.nb_requins_init_max)
energie = 3 # énergie potentiel d'un poisson
chronon = int(initialisation.chronon)
auto_simu = int(initialisation.auto_simu)



def simulation(auto_simu, monde):
    # génération des requins (initialisation)
    for i in range(nb_requins_init):
        nouveau_requin = Requin(monde.newID(), temps_energie_requin, temps_reproduction_requin, monde.initialisation_position_animal())
        monde.ajout_animal(nouveau_requin, nouveau_requin.position)

    # génération des poissons (initialisation)
    for i in range(nb_poissons_init):
        nouveau_poisson = Poisson(monde.newID(), temps_reproduction_poisson, energie, monde.initialisation_position_animal())
        monde.ajout_animal(nouveau_poisson, nouveau_poisson.position)

    if auto_simu == 0:
        os.system("clear")
        print(monde, "init")
    etat_du_monde = [] # permet de sauvegarder l'état du monde à chaque chronon
    tour = 0
    while tour < chronon and monde.nb_animal("P") > 0 and monde.nb_animal("R"):
        tour += 1
        if auto_simu == 0:
            time.sleep(0.1)
            os.system("clear")
        else:
            time.sleep(0)

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

        # gestion de la mort des requins
        indice_animal = 0
        while len(monde.liste_animaux) > indice_animal:
            # cas où l'ANIMAL est arrivé à 0 d'énergie
            if monde.liste_animaux[indice_animal].energie <= 0:
                monde.mort_animal(monde.liste_animaux[indice_animal])
            else:
                indice_animal += 1

        if auto_simu == 0:
            print(monde, tour, "/", chronon)
            print("nombre de poissons :", monde.nb_animal('P'))
            print("nombre de requins :", monde.nb_animal('R'))
        etat_du_monde.append((tour, monde.nb_animal('P'), monde.nb_animal('R'), largeur_monde * hauteur_monde - monde.nb_animal('P') - monde.nb_animal('R')))

    # on ajoute la simulation en BDD
    SQL.new_simulation(monde, tour, chronon, largeur_monde * hauteur_monde - monde.nb_animal("P") - monde.nb_animal("R"))
    SQL.new_simulation_evolution(etat_du_monde)



# script permettant de faire une seule simulation ou plusieurs
if auto_simu == 1:
    for tps_reproduction_poisson in range(temps_reproduction_poisson, temps_reproduction_poisson_max + 1):
        for tps_reproduction_requin in range(temps_reproduction_requin, temps_reproduction_requin_max + 1):
            for tps_energie_requin in range(temps_energie_requin, temps_energie_requin_max + 1):
                for nb_poissons in range(nb_poissons_init, nb_poissons_init_max + 1):
                    for nb_requins in range(nb_requins_init, nb_requins_init_max + 1):
                        # génération du monde vide
                        print("")
                        print("-----------------------------------------------------------")
                        print("")
                        print("tps_reproduction_poisson", tps_reproduction_poisson)
                        print("tps_reproduction_requin", tps_reproduction_requin)
                        print("tps_energie_requin", tps_energie_requin)
                        print("nb_poissons", nb_poissons)
                        print("nb_requins", nb_requins)
                        monde = new_monde.Monde(largeur_monde,
                                            hauteur_monde,
                                            temps_reproduction_poisson,
                                            temps_reproduction_requin,
                                            temps_energie_requin,
                                            nb_poissons_init,
                                            nb_requins_init)
                        simulation(auto_simu, monde)
                        del monde

else:
    # génération du monde vide
    monde = new_monde.Monde(largeur_monde,
                        hauteur_monde,
                        temps_reproduction_poisson,
                        temps_reproduction_requin,
                        temps_energie_requin,
                        nb_poissons_init,
                        nb_requins_init)
    simulation(auto_simu, monde)