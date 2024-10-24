from classes.joueur import Joueur
from classes.inventaire import Inventaire

def arme_in_inventaire(inventaire, arme):
    armes = Inventaire.get_arme(self, inventaire)
    for a in armes:
        if (a == arme):
            return True
    return False

def desequiper():
    arme = Joueur.get_arme(self)
    if (arme != poing):
        Inventaire.ajouter_arme(Joueur.get_inventaire(self))
        Joueur.set_arme(self, poing)

def equiper(arme):
    inventaire = Joueur.get_inventaire(self)
    if arme_in_inventaire(inventaire, arme):
        desequiper()
        Inventaire.supprimer_arme(inventaire, arme)
        Joueur.set_arme(self, arme)

