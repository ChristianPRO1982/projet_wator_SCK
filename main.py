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
chronon = int(initialisation.chronon)
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
    nouveau_poisson = poisson.Poisson(monde.initialisation_position_animal())
    monde.ajout_animal(nouveau_poisson, nouveau_poisson.position)

tour = 0
while tour < chronon:
    print(monde.tableau_monde)

    tour += 1