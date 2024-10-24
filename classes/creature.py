public class Creature():
    def __init__(self,nom:str,race:str,identite,classe,competences,statistiques,butin): #butin creer nouvelle class? 
        self.__nom=nom
        self.__race=race
        self.__classe=classe
        self.__competences=competences
        self.__statistiques=statistiques
        self.__butin=butin
