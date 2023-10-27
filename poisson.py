import random

class Poisson:

    def __init__(self,temps_gestation,energie,position):
        self.energie = energie
        self.position = position
        self.gestation = 0
        self.temps_gestation = temps_gestation
        self.type = "poisson"

    def __str__(self):
        return "P"
    
    def temps_gestation(self):
        self.gestation += 1
        bebe = False
        if self.gestation == self.temps_gestation:
            bebe = True
            self.gestation = 0
        return bebe


    def se_deplacer(self, liste_des_choix, largeur_monde, hauteur_monde):
        ancienne_position = self.position
        direction = random.choice(liste_des_choix)
        if direction == "haut":
            self.position = [self.position[0] + 1, self.position[1]]
            if self.position[0] >= hauteur_monde:
                self.position[0] = 0
        elif direction == "bas":
            self.position = [self.position[0] - 1, self.position[1]]
            if self.position[0] < 0:
                self.position[0] = hauteur_monde - 1
        elif direction == "gauche":
            self.position = [self.position[0], self.position[1] - 1]
            if self.position[1] < 0:
                self.position[1] = largeur_monde - 1
        elif direction == "droit":
            self.position = [self.position[0], self.position[1] + 1]
            if self.position[1] >= largeur_monde:
                self.position[1] = 0
        return ancienne_position, self.position, False#self.temps_gestation()



    
