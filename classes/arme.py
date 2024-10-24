class Arme():
    def __init__(self,attaque=0,rarete="A",prix=1,etat=100,restriction=1,type='poing'): 
        self.__attaque=attaque
        self.__rarete=rarete
        self.__prix=prix
        self.__etat=etat
        self.__restriction=restriction
        self.__type=type

    def get_type(self):
        return self.__type
    
    def set_type(self, type):
        self.__type = type

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
    
