public class Creature():
    def __init__(self,nom:str,race:str,identite,classe,competences,attaque,niv,pv,pvmax,arme,butin): #butin creer nouvelle class? 
        self.__nom=nom
        self.__race=race
        self.__classe=classe
        self.__competences=competences
        self.__attaque=attaque
        self.pv=pv
        self.pvmax=pvmax
        self.niv=niv
        self.arme=arme
        self.__butin=butin

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_race(self):
        return self.__race

    def set_race(self, race):
        self.__race = race

    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe

    def get_competences(self):
        return self.__competences

    def set_competences(self, competences):
        self.__competences = competences

    def get_attaque(self):
        return self.__attaque

    def set_attaque(self, attaque):
        self.__attaque = attaque

    def get_pv(self):
        return self.pv

    def set_pv(self, pv):
        self.pv = pv

    def get_pvmax(self):
        return self.pvmax

    def set_pvmax(self, pvmax):
        self.pvmax = pvmax

    def get_niv(self):
        return self.niv

    def set_niv(self, niv):
        self.niv = niv

    def get_arme(self):
        return self.arme

    def set_arme(self, arme):
        self.arme = arme

    def get_butin(self):
        return self.__butin

    def set_butin(self, butin):
        self.__butin = butin
