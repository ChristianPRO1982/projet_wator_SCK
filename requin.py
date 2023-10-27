from poisson import Poisson

class Requin(Poisson):
    def __init__(self,energie,temps_reproduction_requin,position):
        self.energie = energie
        self.energie_max = energie
        self.naissance = 0
        self.temps_reproduction_requin = temps_reproduction_requin
        self.position = position
        self.type = "requin"

    def __str__(self):
        return "R"
    
        
    def nourrir(self,nourriture):
        self.energie -= nourriture
        return self.energie

    def reproduction(self):
        if self.energie >= self.energie_max and self.naissance < self.temps_reproduction_requin :
            self.naissance += 1
        else:
            pass

    def position_du_requin(self,vouevelle_position):
        self.position = vouevelle_position
        return self.position
    
