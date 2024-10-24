from classes.combattant import Combattant

class Creature(Combattant):
    def __init__(self,nom:str,race,classe,niv,pvmax,pv,attaque,defense,competence,arme,armure,butin): 
        super().__init__(nom,race,classe,niv,pvmax,pv,attaque,defense,competence,arme,armure)
        self.__butin=butin

    def get_butin(self):
        return self.__butin

    def set_butin(self, butin):
        self.__butin = butin
