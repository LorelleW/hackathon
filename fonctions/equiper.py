from classes.joueur import Joueur
from classes.inventaire import Inventaire

def arme_in_inventaire(inventaire, arme):
    armes = Inventaire.get_arme(inventaire)
    for a in armes:
        if (a == arme):
            return True
    return False

def desequiper():
    arme = Joueur.get_arme(joueur)
    if (arme != poing):
        Inventaire.ajouter_arme(Joueur.get_inventaire(joueur))
        Joueur.set_arme(joueur, poing)

def equiper(arme):
    inventaire = Joueur.get_inventaire(joueur)
    if arme_in_inventaire(inventaire, arme):
        desequiper()
        Inventaire.supprimer_arme(inventaire, arme)
        Joueur.set_arme(joueur, arme)
