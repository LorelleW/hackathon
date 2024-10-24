class Armure():
    def __init__(self,type5:str,restriction,defense,rarete,etat:str,prix:int): 
        self.__type5=type5 
        self.__restriction=restriction
        self.__defense=defense
        self.__rarete=rarete
        self.__etat=etat
        self.__prix=prix
        
    def get_type5(self):
        return self.__type5

    def set_type5(self,type5):
        self.__type5=type5

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
        
        
        
        
    

        
