from poisson import Poisson

class Requin(Poisson):
    def __init__(self,ID,energie,temps_reproduction_requin,position):
        self.ID = ID
        self.energie = energie
        self.energie_max = energie
        # self.naissance = 0
        # self.temps_reproduction_requin = temps_reproduction_requin
        self.gestation = 0
        self.temps_gestation = temps_reproduction_requin
        self.position = position
        # self.type = "requin"


    def __str__(self):
        return "R"
    
        
    def nourrir(self,nourriture):
        self.energie -= nourriture
        return self.energie


    # def reproduction(self):
    #     if self.energie >= self.energie_max and self.naissance < self.temps_reproduction_requin :
    #         self.naissance += 1
    #     else:
    #         pass


    def position_du_requin(self,nouevelle_position):
        self.position = nouevelle_position
        return self.position
    

    def liste_des_choix(self, liste_des_choix):
        liste_des_choix_requin_poisson = list() # liste des choix avec un poisson à manger pour un requin
        liste_des_choix_requin_eau = list() # liste des choix de cases vides dans le cas où il n'y a pas de poisson
        energie_max = 0 # variable servant à laisser au requin seulement les cases avec les poissons ayant le plus d'énergie

        for choix in liste_des_choix:
            liste_des_choix_requin_eau.append(choix[0])
            if choix[2] > energie_max:
                liste_des_choix_requin_poisson = list()
                energie_max = choix[2]
            if choix[2] > 0:
                liste_des_choix_requin_poisson.append(choix[1])
        
        if energie_max > 0:
            # cas où il y a des poissons à manger
            return liste_des_choix_requin_poisson
        else:
            # cas où il n'y a pas des poissons à manger
            return liste_des_choix_requin_eau