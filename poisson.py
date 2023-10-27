import random

class Poisson:

    def __init__(self,temps_gestation,energie,position):
        self.energie = energie
        self.position = position
        self.temps=temps_gestation
        self.categorie
        self.temps_gestation=temps_gestation
        self.position = position
    
    def __str__(self):
        return "poisson"
    
    def temps_gestation (self):
        temps_gestation = 0
        self.temps_gestation +=1
        if temps_gestation== 8:
            bebe == True
            temps = 0
        return bebe


    def position(self):
        self.position= [x,y]
        direction = random.choice(liste_des_choix)
        if direction == "haut":
            self.position = [x,y+1]
        elif direction == "bas":
            self.position == [x,y-1]
        elif direction == "gauche":
            self.position = [x-1,y]
        elif direction == "droite":
            self.position = [x+1,y]
        return self.position



    
