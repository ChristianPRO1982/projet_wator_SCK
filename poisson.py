import random

class Poisson:

    def __init__(self, ID : int, temps_gestation : int, energie : int, position : list):
        self.ID = ID
        self.energie = random.randint(energie - 1, energie + 1)
        if self.energie < energie:
            self.image = "poisson1"
        elif self.energie > energie:
            self.image = "poisson3"
        else:
            self.image = "poisson2"
        self.position = position
        self.gestation = 0
        self.temps_gestation = temps_gestation

    def __str__(self) -> str:
        return "P"
    
    def calcul_gestation(self, monde) -> bool:
        # prise en compte de la saison pour le temps de gestation
        temps_gestation_max = self.temps_gestation
        if monde.saison == "été": temps_gestation_max *= 1.1
        if monde.saison == "hiver": temps_gestation_max *= 0.9

        # le temps de gestation peut être stopé selon les conditions de saison, de jour/nuit et d'espèce
        if monde.saison in ("été", "hiver") or \
        monde.saison == "printemps" and ((str(self) == "R" and monde.jour_nuit == 1) or str(self) == "P") or \
        monde.saison == "automne" and ((str(self) == "P" and monde.jour_nuit == 0) or str(self) == "R"):
            self.gestation += 1
        # else:
        #     print(monde.saison, self, monde.jour_nuit)

        bebe = False
        if self.gestation >= temps_gestation_max: #  B U G
            bebe = True
            self.gestation = 0
        return bebe


    # def se_deplacer(self, liste_des_choix):
    #     ancienne_position = self.position
    #     direction = random.choice(liste_des_choix)
    #     if direction == "haut":
    #         self.position = [self.position[0], self.position[1] + 1]
    #     elif direction == "bas":
    #         self.position == [self.position[0], self.position[1] - 1]
    #     elif direction == "gauche":
    #         self.position = [self.position[0] - 1, self.position[1]]
    #     elif direction == "droite":
    #         self.position = [self.position[0] + 1, self.position[1]]
    #     return ancienne_position, self.position, self.temps_gestation()


    def liste_des_choix(self, liste_des_choix_tupple, jour_nuit)->list:
        # on transforme le tuple retourné par la fonction "liste de choix" dans monde.py en liste
        #si l'energie est 0, on ajoute le premier indice qui est la direction
        liste_des_choix_poisson = []
        for choix in liste_des_choix_tupple:
            if choix[1] == "":
                liste_des_choix_poisson.append(choix[0])
        return liste_des_choix_poisson, False


    def se_deplacer(self, liste_des_choix_tupple, largeur_monde, hauteur_monde, jour_nuit, monde) -> list:
        # on sauvegarde l'ancienne position pour que MONDE mette de l'eau ou une naissance dans cette case
        ancienne_position = self.position
        
        # on récupère dans 'liste_des_choix' seulement les cases utiles pour l'animal en question (poisson ou requin)
        liste_des_directions, manger = self.liste_des_choix(liste_des_choix_tupple, jour_nuit)

        # on véridie si l'ANIMAL a la possibilité de se déplacer
        if len(liste_des_directions) > 0:
            # on choisi au hazard une direction dans la liste des choix adpaté à l'animal
            direction = random.choice(liste_des_directions)

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
        

        return ancienne_position, self.position, self.calcul_gestation(monde),manger



  

