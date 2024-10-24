from classes.pnj import Pnj
from classes.joueur import Joueur
from classes.inventaire import Inventaire
from classes.echoppe import Echoppe
'''
def vendre(item):
  inventaire_joueur=Joueur.get_inventaire()
  x=-1
  for liste in (inventaire_joueur):
    x+=1
    if item in liste:
      break;
    else:
      print("Error404")
  if x==0:
    prix=Livre.get.__prix()
  if x==1:
    prix=Armure.get.__prix()
  if x==2:
    prix=Arme.get.__prix()
  if x==3:
    prix=Objet.get.__prix()
  else:
    print("Erreur")
  '''

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
