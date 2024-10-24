class Creature():
    def __init__(self,identite:str,race:str,classe,niv,pvmax,pv,attaque,defense,competence,arme,armure,butin): 
        super().__init__(identite,race,classe,niv,pvmax,pv,attaque,defense,competence,arme,armure)
        self.__butin=butin




    def get_butin(self):
        return self.__butin

    def set_butin(self, butin):
        self.__butin = butin
