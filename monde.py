from random import randint

class Monde:
    def __init__(self,
                 largeur_monde: int,
                 hauteur_monde: int,
                 temps_reproduction_poisson: int,
                 temps_reproduction_requin: int,
                 temps_energie_requin: int,
                 nb_poissons_init: int,
                 nb_requins_init: int) -> None:
        # initialisation des variables
        self.largeur_monde = largeur_monde
        self.hauteur_monde = hauteur_monde
        self.temps_reproduction_poisson = temps_reproduction_poisson
        self.temps_reproduction_requin = temps_reproduction_requin
        self.temps_energie_requin = temps_energie_requin
        self.nb_poissons_init = nb_poissons_init
        self.nb_requins_init = nb_requins_init
        self.ID_animal = 0 # initialisation identifiant
        self.nb_poisson = 0 # nombre de poisson : pour afficher l'état du monde à un instant donné
        self.nb_requin = 0 # nombre de requin : pour afficher l'état du monde à un instant donné
        self.nb_poisson_max = 0 # nombre de poisson au maximum obtenu pendant la simulation
        self.nb_requin_max = 0 # nombre de requin au maximum obtenu pendant la simulation

        # génération du monde
        # /!\ attention : les coordonnées commence à 1 pour aller à "largeur_monde" ou "hauteur_monde"
        #                 et non de 0 à "largeur_monde - 1" ou "hauteur_monde - 1"
        self.tableau_monde = [["¤" for x in range(largeur_monde)] for y in range(hauteur_monde)]
        # génération de la liste des animaux
        self.liste_animaux = []


    def __str__(self) -> str:
        texte = ""
        for ligne in self.tableau_monde:
            for colonne in ligne:
                texte += str(colonne) + " "
            texte += "\n"
        return texte


    def initialisation_position_animal(self):
        while True:
            test_position = [randint(0, self.hauteur_monde - 1), randint(0, self.largeur_monde - 1)] # choix de la colonne / choix de la ligne
            if self.tableau_monde[test_position[0]][test_position[1]] == "¤":
                return test_position


    def newID(self):
        # permet de générer un ID unique par animal
        self.ID_animal += 1
        return self.ID_animal


    def ajout_animal(self, animal, position):
        # on ajoute le nouvel animal dans la "liste des animaux" et dans le "tableau_monde"
        self.liste_animaux.append(animal)
        self.tableau_monde[position[0]][position[1]] = animal
        # on compte les animaux
        if str(animal) == "P": self.nb_poisson += 1
        if str(animal) == "R": self.nb_requin += 1

    
    def liste_de_choix(self, position):
        # génère une liste str avec les mots : ["haut", "bas", "gauche", "droit"]
        # si un poisson existe dans une case, sa valeur nutritive est indiquée en plus
        liste_de_choix = []
        if self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]] == "¤":
            liste_de_choix.append(("haut", "", 0))
        elif self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]] != "¤":
            animal = self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]]
            if str(animal) == 'P':
                liste_de_choix.append(("haut", "poisson", animal.energie))
        
        if self.tableau_monde[(position[0]-1) % self.hauteur_monde][position[1]] == "¤":
            liste_de_choix.append(("bas", "", 0))
        elif self.tableau_monde[(position[0]-1) % self.hauteur_monde][position[1]] != "¤":
            animal = self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]]
            if str(animal) == 'P':
                liste_de_choix.append(("bas", "poisson", animal.energie))
        
        if self.tableau_monde[position[0]][(position[1]+1) % self.largeur_monde] == "¤":
            liste_de_choix.append(("droit", "", 0))
        elif self.tableau_monde[position[0]][(position[1]+1) % self.largeur_monde] != "¤":
            animal = self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]]
            if str(animal) == 'P':
                liste_de_choix.append(("droit", "poisson", animal.energie))
        
        if self.tableau_monde[position[0]][(position[1]-1) % self.largeur_monde] == "¤":
            liste_de_choix.append(("gauche", "", 0))
        elif self.tableau_monde[position[0]][(position[1]-1) % self.largeur_monde] != "¤":
            animal = self.tableau_monde[(position[0]+1) % self.hauteur_monde][position[1]]
            if str(animal) == 'P':
                liste_de_choix.append(("gauche", "poisson", animal.energie))
        
        return liste_de_choix


    def deplacer_animal(self, animal, ancienne_position, nouvelle_position):
        # on déplace dans la nouvelle position le poisson
        # self.tableau_monde[nouvelle_position[0]][nouvelle_position[1]] = str(animal)
        self.tableau_monde[nouvelle_position[0]][nouvelle_position[1]] = animal
        
        # on met de l'eau dans l'ancienne position
        self.tableau_monde[ancienne_position[0]][ancienne_position[1]] = "¤"
    

    def plein(self):
        # pour vérifier qu'il reste au moins une place
        return len(self.liste_animaux)
    

    def animal_mange(self, position):
        # on recherche dans la liste des animaux celui qui est dans la future position de l'animal qui est en train de le manger
        i = 0
        for animal in self.liste_animaux:
            if animal.position[0] == position[0] and animal.position[1] == position[1]:
                index_animal_mange = i
            i += 1
        
        # on supprime de la liste des animaux l'animal mangé
        self.liste_animaux.pop(index_animal_mange)
        print("animal mangé")