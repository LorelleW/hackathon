class Pnj():
    def __init__(self,identite,metier:str,statistiques,inventaire,avisdujoueur): 
        self.__identite=identite
        self.__metier=metier
        self.__statistiques=statistiques
        self.__inventaire=inventaire
        self.__avisdujoueur=avisdujoueur


    def get_identite(self):
        return self.__identite

    def set_identite(self,identite):
        self.__identite=identite

    def get_metier(self):
        return self.__metier

    def set_metier(self,metier):
        self.__metier=metier

    def get_statistiques(self):
        return self.__statistiques

    def set_statistiques(self,statistiques):
        self.__statistiques=statistiques

    def get_inventaire(self):
        return self.__inventaire

    def set_inventaire(self,inventaire):
        self.__inventaire=inventaire

    def get_avisdujoueur(self):
        return self.__avisdujoueur

    def set_avisdujoueur(self,avisdujoueur):
        self.__avisdujoueur=avisdujoueur
