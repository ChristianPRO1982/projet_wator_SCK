import initialisation
import monde
import poisson
import requin

# récupération des variables d'initialisation
largeur_monde = int(initialisation.largeur_monde)
hauteur_monde = int(initialisation.hauteur_monde)
temps_reproduction_poisson = int(initialisation.temps_reproduction_poisson)
temps_reproduction_requin = int(initialisation.temps_reproduction_requin)
temps_energie_requin = int(initialisation.temps_energie_requin)
nb_tour_simulation = int(initialisation.nb_tour_simulation)
nb_poissons_init = int(initialisation.nb_poissons_init)
nb_requins_init = int(initialisation.nb_requins_init)

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
    print("new position", monde.initialisation_position_animal())
    nouveau_poisson = poisson(monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_poisson, [nouveau_poisson.position_colonne, nouveau_poisson.position_ligne])

tour = 0
while tour < nb_tour_simulation:
    print(nouveau_poisson)

    tour += 1