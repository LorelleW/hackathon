import random as rd
from classes.creature import Creature
from classes.objet import Objet
from classes.region import Region
from classes.race import Race
from classes.classe import Classe
from classes.butin import Butin
from classes.arme import *
from classes.armure import *

def generer_slime(niv):
    Neant = Region("autre", 100, {}, 999, "Divinite_inconnue")
    slime = Race("slime", Neant, "D", 50)
    Lac_mort = Region("marais", 0, {slime: 15}, 10, "Slime_king")
    slime.set_region(Lac_mort)
    nomade = Classe("nomade", "nu", "neutre")
    gelee = Objet("gelee", "autre", 2, "organique", "D")
    armure_gluant = Armure("armure_gluant", 8, "C", 5, 100, 1, "torse")
    butin_slime = Butin([], [armure_gluant], [], [gelee], 5)
    noms = ["slime rouge", "slime vert", "slime bleu", "slime jaune"]

    r = rd.randint(0, 3)
    exp = niv * (niv - 1)
    if (r == 0):
        slime = Creature(noms[r], slime, nomade, 1, 0, 40, 40, 18, 0, [], poing, nu, butin_slime)
    elif (r == 1):
        slime = Creature(noms[r], slime, nomade, 1, 0, 50, 50, 8, 0, [], poing, nu, butin_slime)
    elif (r == 2):
        slime = Creature(noms[r], slime, nomade, 1, 0, 40, 40, 8, 10, [], poing, nu, butin_slime)
    else:
        slime = Creature(noms[r], slime, nomade, 1, 0, 50, 50, 18, 10, [], poing, nu, butin_slime)
    slime.add_exp(exp)

    return slime


def generer_loup(niv):
    # Création des instances de base pour les loups
    Foret_sombre = Region("forêt", 10, {}, 20, "Chef de meute")
    loup = Race("loup", Foret_sombre, "C", 70)
    Foret_sombre.__dict__["population"] = {loup: 10}  # Assigner des loups à la forêt
    
    guerrier = Classe("guerrier", "armure légère", "agressif")
    fourrure = Objet("fourrure", "ressource", 15, "organique", "C")
    croc = Objet("croc de loup", "ressource", 5, "organique", "C")
    epee_loup = Arme("epee_loup", 10, "B", 50, 100, 1, "epee")
    butin_loup = Butin([], [], [epee_loup], [fourrure,croc], 10)
    noms = ["loup noir", "loup blanc", "loup bar"]

    # Génération de type de loup basé sur des probabilités spécifiques
    r = rd.random()
    exp = niv * (niv - 1)   # Coefficient d'XP plus élevé pour les loups

    # Probabilités conditionnelles pour chaque type de loup
    if r < 0.6:  # 60% pour le loup noir (type le plus commun)
        loup_creature = Creature(noms[0], loup, guerrier, 1, 0, 60, 60, 17, 0, ["morsure"], poing, nu, butin_loup)
    elif r < 0.9:  # 30% pour le loup blanc
        loup_creature = Creature(noms[1], loup, guerrier, 1, 0, 50, 50, 13, 5, ["griffure"], poing, nu, butin_loup)
    else:  # 10% pour le loup bar (le plus rare et le plus puissant)
        loup_creature = Creature(noms[2], loup, guerrier, 1, 0, 70, 70, 20, 10, ["hurlement"], poing, nu, butin_loup)
    
    # Ajouter de l'expérience à la créature loup
    loup_creature.add_exp(exp)

    return loup_creature



def generer_dragon(niv):
    # Création des instances de base pour le dragon
    Montagne_dragon = Region("montagne", 50, {}, 100, "Ancien dragon")
    dragon_race = Race("dragon", Montagne_dragon, "S", 100)
    Montagne_dragon.__dict__["population"] = {dragon_race: 1}  # Associer le dragon à la région
    
    dragon_classe = Classe("Ancien", "écailles résistantes", "agressif")
    ecaille = Objet("écaille de dragon", "ressource", 100, "organique", "S")
    dent = Objet("dent de dragon", "ressource", 150, "organique", "S")
    fureur_dragon = Arme("fureur_dragon", 17, "S", 100, 100, 1, "fureur")
    butin_dragon = Butin([], [], [fureur_dragon], [dent,ecaille], 100)
    nom = "Dragon de feu"

    # Caractéristiques du dragon
    exp = niv * (niv -1)  # Grande quantité d'XP
    dragon_creature = Creature(nom, dragon_race, dragon_classe, 1, 0, 100, 100, 30, 0, ["souffle de feu"], poing, nu, butin_dragon)

    # Ajouter de l'expérience à la créature dragon
    dragon_creature.add_exp(exp)

    return dragon_creature
