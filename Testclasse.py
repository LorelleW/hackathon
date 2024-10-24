import random as rd

class competence():
    def __init__(self,nom:str,niveau:int,description:str,delai:int):
        self.__nom=nom 
        self.__niveau=niveau
        self.__description=description
        self.__delai=delai

class magie():
    def __init__(self,nom:str,description:str,statistiques,type1:str):
        self.__nom=nom 
        self.__description=description 
        self.__statistiques=statistiques #à voir (?) 
        self.__type1=type1 

class race():
    def __init__(self,nom:str,origine:str,rarete,reputation):
        self.__nom=nom 
        self.__origine=origine 
        self.__rarete=rarete #int? str?
        self.__reputation=reputation #?

class classe():
    def __init__(self,nom:str,caracteristique,type2):
        self.__nom=nom 
        self.__caracteristique=caracteristique
        self.__type2=type2

class region():
    def __init__(self,typedelieu,topographie,population,position,proprietaire:str):
        self.__typedelieu=typedelieu
        self.__topographie=topographie
        self.__population=population
        self.__position=position
        self.__proprietaire=proprietaire 


class objet():
    def __init__(self,nom:str,type3:str,prix:int,materiaux,rarete): 
        self.__nom=nom 
        self.__type3=type3 
        self.__prix=prix 
        self.__materiaux=materiaux
        self.__rarete=rarete


class arme():
    def __init__(self,type4:str,restriction,statistiques,rarete,etat:str): 
        self.__type4=type4
        self.__restriction=restriction
        self.__statistiques=statistiques
        self.__rarete=rarete
        self.__etat=etat 


class armure():
    def __init__(self,type5:str,restriction,statistiques,rarete,etat:str): 
        self.__type5=type5 
        self.__restriction=restriction
        self.__statistiques=statistiques
        self.__rarete=rarete
        self.__etat=etat 


class livre():
    def __init__(self,nom:str,type7:str,prix:int,effets:str,rarete): 
        self.__nom=nom 
        self.__type7=type7
        self.__prix=prix 
        self.__effets=effets 
        self.__rarete=rarete
        

class inventaire():
    def __init__(self,livre,armure,arme,objet):
        self.__livre=livre
        self.__armure=armure
        self.__arme=arme
        self.__objet=objet

        
class joueur():
    def __init__(self,statistiques,identite,race,classe,inventaire,competences):
        self.__statistiques=statistiques
        self.__identite=identite
        self.__race=race
        self.__classe=classe
        self.__inventaire=inventaire
        self.__competences=competences

class butin():
    def __init__(self,livre,armure,arme,objet,argent:int): #mettre un système % de chance
        self.__livre=livre
        self.__armure=armure
        self.__arme=arme
        self.__objet=objet
        self.__argent=argent


class creature():
    def __init__(self,race:str,identite,classe,competences,statistiques,butin): #butin creer nouvelle class? 
        self.__race=race 
        self.__identite=identite
        self.__classe=classe
        self.__competences=competences
        self.__statistiques=statistiques
        self.__butin=butin


class pnj():
    def __init__(self,metier:str,statistiques,inventaire,avisdujoueur): 
        self.__metier=metier 
        self.__statistiques=statistiques
        self.__inventaire=inventaire
        self.__avisdujoueur=avisdujoueur
        
class batiment():
    def __init__(self,):
        self.__nom=nom
        self.__age=age
        self.__architecture
        self.__proprietaire
        self.__context_h

class echoppe():
    def __init__(self,inventaire,argent,batiment:str,type6:str,proprietaire:str): 
        self.__inventaire=inventaire 
        self.__argent=argent 
        self.__batiment=batiment
        self.__type6=type6 
        self.__proprietaire=proprietaire 







