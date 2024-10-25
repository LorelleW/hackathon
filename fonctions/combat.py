import random as rd
from classes.joueur import Joueur
from classes.creature import Creature
from classes.butin import Butin
from fonctions.degat import *
from fonctions.equiper import *

def gagner(joueur, creature):
    butin_creature = creature.get_butin()
    livres = butin_creature.get_livre()
    armes = butin_creature.get_arme()
    armures = butin_creature.get_armure()
    objets = butin_creature.get_objet()

    for livre in livres:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_livre(livre)
            print(f"{livre.get_nom()} ajouté(e) à l'inventaire de {joueur.get_nom()}")
    for arme in armes:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_arme(arme)
            print(f"{arme.get_nom()} ajouté(e) à l'inventaire de {joueur.get_nom()}")
            equiper_arme(joueur, arme)
    for armure in armures:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_armure(armure)
            print(f"{armure.get_nom()} ajouté(e) à l'inventaire de {joueur.get_nom()}")
            equiper_armure(joueur, armure)
    for objet in objets:
        if rd.randint(1, 100) > 50:
            joueur.get_inventaire().ajouter_objet(objet)
            print(f"{objet.get_nom()} ajouté(e) à l'inventaire de {joueur.get_nom()}")

    joueur.set_argent(joueur.get_argent() + butin_creature.get_argent())
    print(f"{joueur.get_nom()} gagne {butin_creature.get_argent()} pièces")
    joueur.add_exp((creature.get_niv() + 1) // 2)
    print(f"{joueur.get_nom()} gagne {(creature.get_niv() + 1) // 2} points d'exp")

def combat(joueur,creature):
    while joueur.get_pv() > 0 and creature.get_pv() > 0:
        print(f"{joueur.get_nom()}({joueur.get_pv()}/{joueur.get_pvmax()})")
        print(f"{creature.get_nom()}({creature.get_pv()}/{creature.get_pvmax()})")
        joueur_attaque_creature(creature, joueur)
        creature_attaque_joueur(joueur, creature)
        print()
    if joueur.get_pv() > 0:
        gagner(joueur, creature)
