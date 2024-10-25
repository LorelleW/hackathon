import random as rd
from classes.joueur import Joueur
from classes.creature import Creature
from classes.butin import Butin
from fonctions.degat import *

def gagner(joueur, creature):
    butin_creature = creature.get_butin()
    livres = butin_creature.get_livre()
    armes = butin_creature.get_arme()
    armures = butin_creature.get_armure()
    objets = butin_creature.get_objets()

    for livre in livres:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_livre(livre)
    for arme in armes:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_arme(arme)
    for armure in armures:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_armure(armure)
    for objet in objets:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_objet(objet)

    joueur.set_argent(joueur.set_argent() + butin_creature.get_argent())
    joueur.add_exp(creature.get_niv() / 2)

def combat(joueur,creature):
    while joueur.get_pv() > 0 and creature.get_pv() > 0:
        joueur_attaque_creature(creature, joueur)
        creature_attaque_joueur(joueur, creature)
    if joueur.get_pv() > 0:
        gagner(joueur, creature)
    
