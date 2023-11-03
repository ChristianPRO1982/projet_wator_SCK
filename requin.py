from poisson import Poisson

class Requin(Poisson):
    def __init__(self, ID, energie, temps_reproduction_requin, position, energie_requin_cannibale):
        self.ID = ID
        self.energie = energie
        self.energie_max = energie
        self.gestation = 0
        self.temps_gestation = temps_reproduction_requin
        self.position = position
        self.energie_requin_cannibale = energie_requin_cannibale
        self.image = "requin"


    def __str__(self):
        return "R"
    
    #  creer une methode pour nourrir le requin
    def nourrir(self,nourriture):
        self.energie += nourriture
        if self.energie > self.energie_max:
            self.energie = self.energie_max


    #  on va creer une methode pour baisser l'enrgie du requin s'il mange pas
    def baisse_energie(self):
        self.energie -= 1
        self.image = "requin"
        if self.energie <= self.energie_requin_cannibale:
            self.image = "requin_cannibale"




    def liste_des_choix(self, liste_des_choix, jour_nuit):
        energie_max = 0
        liste_des_choix_poisson = []
        liste_des_choix_eau = []
        for choix in liste_des_choix:
            if (str(choix[1]) == 'P' or (str(choix[1]) == 'R' and self.image == "requin_cannibale")) and jour_nuit == 0:
                if choix[1].energie > energie_max:
                    energie_max = choix[1].energie
                    liste_des_choix_poisson.clear()
                    
                liste_des_choix_poisson.append(choix[0])

            else:
                liste_des_choix_eau.append(choix[0])
                
        if len(liste_des_choix_poisson) == 0:
            return liste_des_choix_eau, False
        else:
            return liste_des_choix_poisson, True