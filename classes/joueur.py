from classes.combattant import Combattant

class Joueur(Combattant):
    def __init__(self,nom,race,classe,niv,pvmax,pv,attaque,defense,competence,argent,inventaire,arme,armure):
        super().__init__(identite,race,classe,niv,pvmax,pv,attaque,defense,competence,arme,armure)
        self.__argent=argent
        self.__inventaire=inventaire


    # Getter et Setter pour argent
    def get_argent(self):
        return self.__argent

    def set_argent(self, argent):
        self.__argent = argent


    # Getter et Setter pour inventaire
    def get_inventaire(self):
        return self.__inventaire

    def set_inventaire(self, inventaire):
        self.__inventaire = inventaire

