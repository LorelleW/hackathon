from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.arme import *

def desequiper_arme(joueur):
    arme = Joueur.get_arme(joueur)
    if (arme != poing):
        Inventaire.ajouter_arme(Joueur.get_inventaire(joueur), arme)
        Joueur.set_arme(joueur, poing)

def equiper_arme(joueur, arme):
    inventaire = Joueur.get_inventaire(joueur)
    if Inventaire.arme_in(inventaire, arme):
        desequiper_arme(joueur)
        Inventaire.retirer_arme(inventaire, arme)
        Joueur.set_arme(joueur, arme)

def desequiper_armure(joueur):
    armure = Joueur.get_armure(joueur)
    if (armure != poing):
        Inventaire.ajouter_armure(Joueur.get_inventaire(joueur), armure)
        Joueur.set_armure(joueur, poing)

def equiper_armure(joueur, armure):
    inventaire = Joueur.get_inventaire(joueur)
    if Inventaire.armure_in(inventaire, armure):
        desequiper_armure(joueur)
        Inventaire.retirer_armure(inventaire, armure)
        Joueur.set_armure(joueur, armure)
