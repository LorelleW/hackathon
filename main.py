import random as rd

#type {1:magie; 2:classe; 3:objet; 4:arme; 5:armure; 6:echoppe; 7:livre}

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
    def __init__(self,nom:str,region:str,rarete,reputation):
        self.__nom=nom 
        self.__region=region 
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
    def __init__(self,nom:str,type3:str,prix:int,materiaux:str,rarete:str): 
        self.__nom=nom 
        self.__type3=type3
        self.__prix=prix
        self.__materiaux=materiaux
        self.__rarete=rarete


class arme():
    def __init__(self,type4:str,restriction,attaque,rarete,etat:str): 
        self.__type4=type4
        self.__restriction=restriction
        self.__attaque=attaque
        self.__rarete=rarete
        self.__etat=etat


class armure():
    def __init__(self,type5:str,restriction,defense,rarete,etat:str): 
        self.__type5=type5 
        self.__restriction=restriction
        self.__defense=defense
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
    def __init__(self,livre,armure,arme,objet): #mettre un système % de chance
        self.__livre=livre
        self.__armure=armure
        self.__arme=arme
        self.__objet=objet
        
class guerrier(): 
    def _init_(self,race,niv,pvmax,pv,attaque,defense,argent,classe,competence,statistique,identite):
        self.__race = race
        self.__classe = classe
        self.__competence = competence
        self.__niv=niv
        self.__pvmax=pvmax
        self.__pv=pv
        self.__attaque=attaque
        self.__defense=defense
        self.__argent=argent
        self.__identite = identite

class joueur():
    def __init__(self,niv,pvmax,pv,attaque,defense,argent,identite,race,classe,inventaire,competences,arme,armure):
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


class butin():
    def __init__(self,livre,armure,arme,objet,argent:int): #mettre un système % de chance
        self.__livre=livre
        self.__armure=armure
        self.__arme=arme
        self.__objet=objet
        self.__argent=argent


class creature():
    def __init__(self,nom:str,race:str,identite,classe,competences,statistiques,butin): #butin creer nouvelle class? 
        self.__nom=nom
        self.__race=race
        self.__classe=classe
        self.__competences=competences
        self.__statistiques=statistiques
        self.__butin=butin


class pnj():
    def __init__(self,identite,metier:str,statistiques,inventaire,avisdujoueur): 
        self.__identite=identite
        self.__metier=metier
        self.__statistiques=statistiques
        self.__inventaire=inventaire
        self.__avisdujoueur=avisdujoueur
        
class batiment():
    def __init__(self,nom:str,age:int,architecture,proprietaire,context_h):
        self.__nom=nom
        self.__age=age
        self.__architecture=architecture
        self.__proprietaire=proprietaire
        self.__context_h=context_h

class echoppe():
    def __init__(self,inventaire,argent,batiment:str,type6:str,proprietaire:str): 
        self.__inventaire=inventaire 
        self.__argent=argent
        self.__batiment=batiment
        self.__type6=type6 
        self.__proprietaire=proprietaire 

class effets():
    def __init__(self,nom:str,description:str):
        self.__nom=nom 
        self.__description=description



