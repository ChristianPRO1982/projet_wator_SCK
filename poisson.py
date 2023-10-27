import random

class Poisson:

    def __init__(self,temps_gestation,energie,position):
        self.energie = energie
        self.position = position
        self.gestation = 0
        self.temps_gestation = temps_gestation

    def __str__(self):
        return "P"
    
    def temps_gestation(self):
        self.gestation += 1
        bebe = False
        if self.gestation == self.temps_gestation:
            bebe = True
            self.gestation = 0
        return bebe


    def position(self, liste_des_choix):
        ancienne_position = self.position
        direction = random.choice(liste_des_choix)
        if direction == "haut":
            self.position = [self.position[0], self.position[1] + 1]
        elif direction == "bas":
            self.position == [self.position[0], self.position[1] - 1]
        elif direction == "gauche":
            self.position = [self.position[0] - 1, self.position[1]]
        elif direction == "droite":
            self.position = [self.position[0] + 1, self.position[1]]
        return ancienne_position, self.position, self.temps_gestation()



    
