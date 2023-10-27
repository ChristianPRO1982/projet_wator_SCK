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
                texte += colonne + " "
            texte += "\n"
        return texte


    def initialisation_position_animal(self):
        while True:
            test_position = [randint(0, self.hauteur_monde - 1), randint(0, self.largeur_monde - 1)] # choix de la colonne / choix de la ligne
            print(test_position)
            if self.tableau_monde[test_position[0]][test_position[1]] == "¤":
                return test_position


    def newID(self):
        # permet de générer un ID unique par animal
        self.ID_animal += 1
        return self.ID_animal


    def ajout_animal(self, animal, position):
        # on ajoute le nouvel animal dans la "liste des animaux" et dans le "tableau_monde"
        self.liste_animaux.append(animal)
        self.tableau_monde[position[0]][position[1]] = str(animal)

    
    def liste_de_choix(self, position):
        # ["haut", "bas", "gauche", "droit"]
        # []
        liste_de_choix = []
        if self.tableau_monde[(position[0]+1) % self.largeur_monde][position[1]] == "¤":
            liste_de_choix.append("droit")
        if self.tableau_monde[(position[0]-1) % self.largeur_monde][position[1]] == "¤":
            liste_de_choix.append("gauche")
        if self.tableau_monde[position[0]][(position[1]+1) % self.hauteur_monde] == "¤":
            liste_de_choix.append("haut")
        if self.tableau_monde[position[0]][(position[1]-1) % self.hauteur_monde] == "¤":
            liste_de_choix.append("bas")
        return liste_de_choix


    def deplacer_poisson(self, ancienne_position, nouvelle_position):
        # on déplace dans la nouvelle position le poisson
        print(ancienne_position, nouvelle_position)
        self.tableau_monde[nouvelle_position[0], nouvelle_position[1]] = self.tableau_monde[ancienne_position[0], ancienne_position[1]]
        
        # si le poisson s'est déplacé alors on met de l'eau dans l'ancienne position
        if ancienne_position != nouvelle_position:
            self.tableau_monde[ancienne_position[0], ancienne_position[1]] = "¤"
            return True # autorisation à faire une naissance
        
        return False # interdiction à faire une naissance