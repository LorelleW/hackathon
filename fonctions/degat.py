from classes.arme import Arme
from classes.joueur import Joueur
from classes.creature import Creature
import random as rd

def degat_joueur(joueur, creature):
  attaque_joueur = joueur.get_attaque()
  attaque_arme_joueur = joueur.get_arme().get_attaque()
  defense_creature = creature.get_defense()
  defense_armure_creature = creature.get_armure().get_defense()
  return max(1, (attaque_joueur + attaque_arme_joueur) - (defense_creature + defense_armure_creature))

def degat_creature(creature, joueur):
  attaque_creature = creature.get_attaque()
  attaque_arme_creature = creature.get_arme().get_attaque()
  defense_joueur = joueur.get_defense()
  defense_armure_joueur = joueur.get_armure().get_defense()

  chance = rd.randint(1,100)
  
  if chance <= 20: 
    return (0)
  return max(1, (attaque_creature + attaque_arme_creature) - (defense_joueur + defense_armure_joueur))

def creature_attaque_joueur(joueur, creature):
  pv = joueur.get_pv()
  degat = degat_creature(creature, joueur)
  pv -= degat
  print(f"{creature.get_nom()} inflige {degat} à {joueur.get_nom()}")
  joueur.set_pv(pv)
  if (pv <= 0):
    print("Tu es mort...")
  return degat

def joueur_attaque_creature(creature, joueur):
  pv = creature.get_pv()
  degat = degat_joueur(joueur, creature)
  pv -= degat
  print(f"{joueur.get_nom()} inflige {degat} à {creature.get_nom()}")
  creature.set_pv(pv)
  if (pv <= 0):
    print("Vous avez vaincu le monstre")
  return degat

def joueur_utiliser_competence(creature, joueur, mult):
  pv = creature.get_pv()
  degat = degat_joueur(joueur, creature) * mult
  pv -= degat
  print(f"{joueur.get_nom()} inflige {degat} à {creature.get_nom()}")
  creature.set_pv(pv)
  if (pv <= 0):
    print("Vous avez vaincu le monstre")
  return degat
