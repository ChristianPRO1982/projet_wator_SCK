class Requin(Poisson):
    def __init__(self,energie,naissance,temps_reproduction_requin,alimentation,position):
        self.energie = energie
        self.naissance = naissance
        self.temps_reproduction_requin = temps_reproduction_requin
        self.alimentation = alimentation
        self.position = position
        self.energie_max = energie

    def __st__(self):
        return f"requin et poisson "
    
        
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
    
