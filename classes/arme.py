class Arme():
    def __init__(self,type4='poing':str,restriction,attaque=0:int,rarete,etat:str,prix:str): 
        self.__type4=type4
        self.__restriction=restriction
        self.__attaque=attaque
        self.__rarete=rarete
        self.__etat=etat
        self.__prix=prix

    def get_type4(self):
        return self.__type4
    
    def set_type4(self, type4):
        self.__type4 = type4 

    def get_prix(self):
        return self.__prix
    
    def set_prix(self, prix):
        self.__prix = prix

    def get_restriction(self):
        return self.__restriction

    def set_restriction(self, restriction):
        self.__restriction = restriction

    def get_attaque(self):
        return self.__attaque

    def set_attaque(self,attaque):
        self._attaque = attaque

    def get_rarete(self):
        return self.__rarete

    def set_rarete(self,rarete):
        self._rarete = rarete

    def get_etat(self):
        return self.__etat

    def set_etat(self,etat):
        self.__etat = etat 
    
