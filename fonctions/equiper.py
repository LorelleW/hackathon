from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.arme import *

def desequiper_arme(joueur):
    arme = joueur.get_arme()
    if (arme != poing):
        joueur.get_inventaire().ajouter_arme(arme)
        joueur.set_arme(poing)

def equiper_arme(joueur, arme):
    inventaire = joueur.get_inventaire()
    if inventaire.arme_in(arme):
        desequiper_arme(joueur)
        inventaire.retirer_arme(arme)
        joueur.set_arme(arme)

def desequiper_armure(joueur):
    armure = joueur.get_armure()
    if (armure != poing):
        joueur.get_inventaire().ajouter_armure(armure)
        joueur.set_armure(poing)

def equiper_armure(joueur, armure):
    inventaire = joueur.get_inventaire()
    if inventaire.armure_in(armure):
        desequiper_armure(joueur)
        inventaire.retirer_armure(armure)
        joueur.set_armure(armure)
