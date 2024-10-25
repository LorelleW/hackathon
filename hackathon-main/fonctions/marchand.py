from classes.pnj import Pnj
from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.echoppe import Echoppe

def vendre_livres(livre,joueur):
  prix=livre.get_prix()
  joueur.set_argent(joueur.get_argent()+prix)
  joueur.get_inventaire().retirer_livre(livre)

def vendre_armures(armure,joueur):
  prix=armure.get_prix()
  joueur.set_argent(joueur.get_argent()+prix)
  joueur.get_inventaire().retirer_armure(armure)

def vendre_armes(arme,joueur):
  prix=arme.get_prix()
  joueur.set_argent(joueur.get_argent()+prix)
  joueur.get_inventaire().retirer_arme(arme)

def vendre_objets(objet,joueur):
  prix=objet.get_prix()
  joueur.set_argent(joueur.get_argent()+prix)
  joueur.get_inventaire().retirer_objet(objet)

def acheter_livres(livre,joueur):
  prix=livre.get_prix()
  if joueur.get_argent()>=prix:
    joueur.set_argent(joueur.get_argent()-prix)
    joueur.get_inventaire().ajouter_livre(livre)
  else:
    print("Vous n'avez pas assez!!!")

def acheter_armures(armure,joueur):
  prix=armure.get_prix()
  if joueur.get_argent()>=prix:
    joueur.set_argent(joueur.get_argent()-prix)
    joueur.get_inventaire().ajouter_armure(armure)
  else:
    print("Vous n'avez pas assez!!!")

def acheter_armes(arme,joueur):
  prix=arme.get_prix()
  if joueur.get_argent()>=prix:
    joueur.set_argent(joueur.get_argent()-prix)
    joueur.get_inventaire().ajouter_arme(arme)
  else:
    print("Vous n'avez pas assez!!!")

def acheter_objets(objet,joueur):
  prix=objet.get_prix()
  if joueur.get_argent()>=prix:
    joueur.set_argent(joueur.get_argent()-prix)
    joueur.get_inventaire().ajouter_objet(objet)
  else:
    print("Vous n'avez pas assez!!!")
