import random

class Poisson:

    def __init__(self,ID,temps_gestation,energie,position):
        self.ID = ID
        self.energie = energie
        self.position = position
        self.gestation = 0
        self.temps_gestation = temps_gestation
        # self.type = "poisson"

    def __str__(self):
        return "P"
    
    def calcul_gestation(self):
        self.gestation += 1
        bebe = False
        if self.gestation == self.temps_gestation:
            bebe = True
            self.gestation = 0
        return bebe
    

    def liste_des_choix(self, liste_des_choix):
        liste_des_choix_poisson = []
        for choix in liste_des_choix:
            if choix[2] == 0:
                liste_des_choix_poisson.append(choix[0])
        return liste_des_choix_poisson


    def se_deplacer(self, liste_des_choix, largeur_monde, hauteur_monde):
        # on sauvegarde l'ancienne position pour que MONDE mette de l'eau ou une naissance dans cette case
        ancienne_position = self.position
        
        # on récupère dans 'liste_des_choix' seulement les cases utiles pour l'animal en question (poisson ou requin)
        liste_des_choix = self.liste_des_choix(liste_des_choix)

        # on véridie si l'ANIMAL a la possibilité de se déplacer
        if len(liste_des_choix) > 0:
            # on choisi au hazard une direction dans la liste des choix adpaté à l'animal
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
        

        return ancienne_position, self.position, self.calcul_gestation()



    
