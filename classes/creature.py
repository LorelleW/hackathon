public class Creature():
    def __init__(self,nom:str,race:str,identite,classe,competences,attaque,niv,pv,butin): #butin creer nouvelle class? 
        self.__nom=nom
        self.__race=race
        self.__classe=classe
        self.__competences=competences
        self.__attaque=attaque
        self.pv=pv
        self.niv=niv
        self.__butin=butin
