from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.arme import *

def desequiper_arme(joueur):
    arme = joueur.get_arme()
    if (arme != poing):
        joueur.get_inventaire().ajouter_arme(arme)
        joueur.set_arme(poing)
        print(f"{arme.get_nom()} desequipee de {joueur.get_nom()}")

def equiper_arme(joueur, arme):
    inventaire = joueur.get_inventaire()
    if inventaire.arme_in(arme):
        desequiper_arme(joueur)
        inventaire.retirer_arme(arme)
        joueur.set_arme(arme)
        print(f"{arme.get_nom()} equipee à {joueur.get_nom()}")
    else:
        print(f"{arme.get_nom()} n'est pas dans l'inventaire de {joueur.get_nom()}")

def desequiper_armure(joueur):
    armure = joueur.get_armure()
    if (armure != poing):
        joueur.get_inventaire().ajouter_armure(armure)
        joueur.set_armure(poing)
        print(f"{armure.get_nom()} desequipee de {joueur.get_nom()}")

def equiper_armure(joueur, armure):
    inventaire = joueur.get_inventaire()
    if inventaire.armure_in(armure):
        desequiper_armure(joueur)
        inventaire.retirer_armure(armure)
        joueur.set_armure(armure)
        print(f"{armure.get_nom()} equipee à {joueur.get_nom()}")
    print(f"{armure.get_nom()} n'est pas dans l'inventaire de {joueur.get_nom()}")

