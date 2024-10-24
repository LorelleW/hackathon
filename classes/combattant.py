from classes.arme import *
from classes.armure import *

class Combattant(): 
    def __init__(self,identite,race,classe,niv,pvmax,pv,attaque,defense,competence,arme=poing,armure=nu):
        self.__identite = identite
        self.__race = race
        self.__classe = classe
        self.__niv=niv
        self.__pvmax=pvmax
        self.__pv=pv
        self.__attaque=attaque
        self.__defense=defense
        self.__competence = competence
        self.__arme=arme
        self.__armure=armure

    def get_identite(self):
        return self.__identite

    def set_identite(self, identite):
        self.__identite = identite
    
    def get_race(self):
        return self.__race

    def set_race(self,race):
        self.__race = race

    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe


    def get_niv(self):
        return self.__niv

    def set_niv(self, niv):
        self.__niv = niv

    def get_pvmax(self):
        return self.__pvmax

    def set_pvmax(self, pvmax):
        self.__pvmax = pvmax

    def get_pv(self):
        return self.__pv

    def set_pv(self, pv):
        self.__pv = pv

    def get_attaque(self):
        return self.__attaque

    def set_attaque(self, attaque):
        self.__attaque = attaque

    def get_defense(self):
        return self.__defense

    def set_defense(self, defense):
        self.__defense = defense

    def get_competence(self):
        return self.__competence

    def set_competence(self, competence):
        self.__competence = competence

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

    def ajouter_competence(self, nouvelle_competence):
        if nouvelle_competence not in self.__competence:
            self.__competence.append(nouvelle_competence)
            print(f"Compétence '{nouvelle_competence}' ajoutée.")
        else:
            print(f"Compétence '{nouvelle_competence}' est déjà présente.")

    def supprimer_competence(self, competence_a_supprimer):
        if competence_a_supprimer in self.__competence:
            self.__competence.remove(competence_a_supprimer)
            print(f"Compétence '{competence_a_supprimer}' supprimée.")
        else:
            print(f"Compétence '{competence_a_supprimer}' n'existe pas dans la liste.")
