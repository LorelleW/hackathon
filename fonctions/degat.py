
from classes.arme import *
from classes.joueur import *
from classes.creature import *

attaque_joueur=joueur.get_attaque(self)
attaque_arme_joueur=arme.get_attaque(joueur.arme) #str nom arme 

attaque_creature=creature.get_attaque(self)
attaque_arme_creature=arme.get_attaque(creature.arme)

def degat_joueur():
  return (attaque_joueur+attaque_arme_joueur)

def degat_creature():
  return (attaque_creature+attaque_arme_creature)
