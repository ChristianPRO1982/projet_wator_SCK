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
        liste_des_choix_poisson = []
        liste_des_choix_eau = []
        for choix in liste_des_choix:
            if choix[1] == 'poisson':
                liste_des_choix_poisson.append(choix[0])
            
            else:
                liste_des_choix_eau.append(choix[0])
                
        if len(liste_des_choix_poisson) == 0:
            return liste_des_choix_eau, False
        else:
            return liste_des_choix_poisson, True