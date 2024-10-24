class Armure():
    def __init__(self,defense=0,rarete="A",prix=1,etat=100,restriction=1,type='nu'): 
        self.__defense=defense
        self.__rarete=rarete
        self.__prix=prix
        self.__etat=etat
        self.__restriction=restriction
        self.__type=type
        
    def get_type(self):
        return self.__type

    def set_type(self,type):
        self.__type=type

    def get_prix(self):
        return self.__prix

    def set_prix(self,prix):
        self.__prix=prix

    def get_restriction(self):
        return self.__restriction

    def set_restriction(self,restriction):
        self.__restriction=restriction

    def get_defense(self):
        return self.__defense

    def set_defense(self,defense):
        self.__defense=defense

    def get_rarete(self):
        return self.__rarete

    def set_rarete(self,rarete):
        self.__rarete = rarete

    def get_etat(self):
         return self.__etat

    def set_etat(self,etat):
        self.__etat=etat
        
        
        
        
    

        
