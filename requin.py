from poisson import Poisson

class Requin(Poisson):
    def __init__(self,ID,energie,temps_reproduction_requin,position):
        self.ID = ID
        self.energie = energie
        self.energie_max = energie
        self.gestation = 0
        self.temps_gestation = temps_reproduction_requin
        self.position = position



    def __str__(self):
        return "R"
    
    #  creer une methode pour nourrir le requin
    def nourrir(self,nourriture):
        self.energie += nourriture


    #  on va creer une methode pour baisser l'enrgie du requin s'il mange pas
    def baisse_energie(self):
        self.energie -= 1


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