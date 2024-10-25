import random as rd
from classes.competence import Competence
from classes.magie import Magie
from classes.race import Race
from classes.classe import Classe
from classes.region import Region
from classes.objet import Objet
from classes.arme import *
from classes.armure import *
from classes.livre import Livre
from classes.inventaire import Inventaire
from classes.combattant import Combattant    
from classes.joueur import Joueur
from classes.butin import Butin
from classes.creature import Creature
from classes.pnj import Pnj
from classes.batiment import Batiment
from classes.echoppe import Echoppe
from classes.effets import Effets
from fonctions.degat import *
from fonctions.equiper import *
from fonctions.marchand import *
from fonctions.combat import *
from fonctions.generation_creature import *

Neant = Region("autre", 100, {}, 999, "Divinite_inconnue")

humain = Race("humain", Neant, "D", 50)
slime = Race("slime", Neant, "D", 50)

Cocorico = Region("ville", 10, {humain: 100}, 50, "Zelda")
humain.set_region(Cocorico)

Lac_mort = Region("marais", 0, {slime: 15}, 10, "Slime_king")
slime.set_region(Lac_mort)

epeiste = Classe("epeiste", "epee", "degat")

couronne = Objet("couronne", "accessoire", 1000, "or", "S")
gelee = Objet("gelee", "autre", 1, "organique", "D")

epee_bois = Arme("epee_bois", 5, "F", 1, 100, 1, "epee")
armure_bois = Armure("armure_bois", 5, "F", 1, 99, 1, "haut")

inventaire_Zelda = Inventaire([], [], [], [couronne])
Zelda = Pnj("Zelda", "civil", 18, inventaire_Zelda)

force = Competence("force", 1, "attaque * 1.5", 5)

inventaire_Link = Inventaire([], [], [], [])
butin_slime = Butin([], [], [], [gelee], 1)

Link = Joueur("Link", humain, epeiste, 1, 0, 100, 100, 10, 5, [force], 10, inventaire_Link, epee_bois, armure_bois)

slime1 = generer_slime(5)
print(slime1.get_nom())
print(slime1.get_niv())
print(slime1.get_exp())
print(slime1.get_pvmax())
print(slime1.get_pv())
print(slime1.get_attaque())
print(slime1.get_defense())
print()

Link.add_exp(20)

combat(Link, slime1)
