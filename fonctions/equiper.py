from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.arme import *

def arme_in_inventaire(inventaire, arme):
    armes = Inventaire.get_arme(inventaire)
    for a in armes:
        if (a == arme):
            return True
    return False

def desequiper_arme(joueur):
    arme = Joueur.get_arme(joueur)
    if (arme != poing):
        Inventaire.ajouter_arme(Joueur.get_inventaire(joueur), arme)
        Joueur.set_arme(joueur, poing)

def equiper_arme(joueur, arme):
    inventaire = Joueur.get_inventaire(joueur)
    if arme_in_inventaire(inventaire, arme):
        desequiper_arme(joueur)
        Inventaire.supprimer_arme(inventaire, arme)
        Joueur.set_arme(joueur, arme)
