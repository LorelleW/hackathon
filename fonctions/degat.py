
from classes.arme import Arme
from classes.joueur import Joueur
from classes.creature import Creature



def degat_joueur():
  attaque_joueur=Joueur.get_attaque()
  arme_joueur = Joueur.get_arme()  # Pas besoin de passer 'joueur' ici
  attaque_arme_joueur = arme_joueur.get_attaque() #str nom arme 
  return (attaque_joueur+attaque_arme_joueur )

def degat_creature():
  attaque_creature=Creature.get_attaque()
  arme_creature = Creature.get_arme()  # Pas besoin de passer 'joueur' ici
  attaque_arme_creature=arme_creature.get_attaque()
  defense_joueur=Joueur.get_defense()
  armure_joueur=Joueur.get_armure()
  defense_armure_joueur = armure_joueur.get_defense()
  return (attaque_creature+attaque_arme_creature - (defense_joueur + defense_armure_joueur))

def pv_actuel_joueur():
  pv_joueur=Joueur.get_pv()
  degat_creat=degat_creature()
  pv_joueur -= degat_creat
  Joueur.set_pv(pv_joueur)
  if (pv_joueur>0):
    return (pv_joueur)
  else:
    print("Tu es mort...")

def pv_actuel_creature():
  pv_creature=Creature.get_pv()
  degat_joueur=degat_joueur()
  pv_creature -= degat_joueur
  Creature.set_pv(pv_creature)
  if (pv_creature<=0):
    print("Vous avez vaincu le monstre")
