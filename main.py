import initialisation
import monde
import poisson
import requin

# récupération des variables d'initialisation
largeur_monde = int(initialisation.largeur_monde)
hauteur_monde = int(initialisation.hauteur_monde)
temps_reproduction_poisson = int(initialisation.temps_reproduction_poisson)
temps_reproduction_requin = int(initialisation.temps_reproduction_requin)
temps_starvation_requin = int(initialisation.temps_starvation_requin)
nb_tour_simulation = int(initialisation.nb_tour_simulation)
nb_poissons_init = int(initialisation.nb_poissons_init)
nb_requins_init = int(initialisation.nb_requins_init)

# initialisation 

# génération du monde vide
monde = monde.Monde(largeur_monde, hauteur_monde, nb_poissons_init, nb_requins_init)

# génération des poissons (initialisation)
for i in range(nb_poissons_init):
    monde.ajout_animal()

tour = 0
while tour < nb_tour_simulation:
    for poisson in monde.liste_poissons
    coordonnes = poisson.coordonnees()
    etat_haut, etat_bas, etat_droit, etat_gauche = monde.etat_positions(coordonnees)
    poisson.chronon(etat_haut, etat_bas, etat_droit, etat_gauche)

    tour += 1