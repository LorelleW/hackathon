
from classes.arme import Arme
from classes.joueur import Joueur
from classes.creature import Creature

attaque_joueur=Joueur.get_attaque(self)
attaque_arme_joueur=Arme.get_attaque(Joueur.get_arme(self)) #str nom arme 

attaque_creature=Creature.get_attaque(self)
attaque_arme_creature=Arme.get_attaque(Creature.get_arme(self))

def degat_joueur():
  return (attaque_joueur+attaque_arme_joueur)

def degat_creature():
  return (attaque_creature+attaque_arme_creature)

def pv_actuel_joueur():
  pv_joueur=joueur.get_pv(self)
  degat_creat=degat_creature()
  pv_joueur -= degat_creat
  joueur.set_pv(self,pv_joueur)
  if (pv_joueur>0):
    return (pv_joueur)
  else:
    print("Tu es mort...")

def pv_actuel_creature():
  pv_creature=creature.get_pv(self)
  degat_joueur=degat_joueur()
  pv_creature -= degat_joueur
  creature.set_pv(self,pv_creature)
  if (pv_creature<=0):
    print("Vous avez vaincu le monstre")
