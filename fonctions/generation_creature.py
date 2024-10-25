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
    butin_slime = Butin([], [], [], [gelee], 5)
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
