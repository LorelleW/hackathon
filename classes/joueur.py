public class Joueur():
    def __init__(self,niv=0:int,pvmax,pv,attaque,defense,argent,identite,race,classe,inventaire,competences,arme='poing':str,armure='sans armure':str):
        self.__niv=niv
        self.__pvmax=pvmax
        self.__pv=pv
        self.__attaque=attaque
        self.__defense=defense
        self.__argent=argent
        self.__identite=identite
        self.__race=race
        self.__classe=classe
        self.__inventaire=inventaire
        self.__competences=competences
        self.__arme=arme
        self.__armure=armure


    # Getter et Setter pour niv
    def get_niv(self):
        return self.__niv

    def set_niv(self, niv):
        self.__niv = niv

    # Getter et Setter pour pvmax
    def get_pvmax(self):
        return self.__pvmax

    def set_pvmax(self, pvmax):
        self.__pvmax = pvmax

    # Getter et Setter pour pv
    def get_pv(self):
        return self.__pv

    def set_pv(self, pv):
        self.__pv = pv

    # Getter et Setter pour attaque
    def get_attaque(self):
        return self.__attaque

    def set_attaque(self, attaque):
        self.__attaque = attaque

    # Getter et Setter pour defense
    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        self.__defense = defense

    # Getter et Setter pour argent
    def get_argent(self):
        return self.__argent

    def set_argent(self, argent):
        self.__argent = argent

    # Getter et Setter pour identite
    def get_identite(self):
        return self.__identite

    def set_identite(self, identite):
        self.__identite = identite

    # Getter et Setter pour race
    def get_race(self):
        return self.__race

    def set_race(self, race):
        self.__race = race

    # Getter et Setter pour classe
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe

    # Getter et Setter pour inventaire
    def get_inventaire(self):
        return self.__inventaire

    def set_inventaire(self, inventaire):
        self.__inventaire = inventaire

    # Getter et Setter pour competences
    def get_competences(self):
        return self.__competences

    def set_competences(self, competences):
        self.__competences = competences

    # Getter et Setter pour arme
    def get_arme(self):
        return self.__arme

    def set_arme(self, arme):
        self.__arme = arme

    # Getter et Setter pour armure
    def get_armure(self):
        return self.__armure

    def set_armure(self, armure):
        self.__armure = armure
