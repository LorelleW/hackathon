import pygame
import random as rd
import time

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


force = Competence("force", 1, 20, 0, 0, 0, 3, [])

inventaire_Link = Inventaire([], [], [], [])
butin_slime = Butin([], [], [], [gelee], 1)

Link = Joueur("Link", humain, epeiste, 1, 0, 100, 100, 10, 5, [force], 10, inventaire_Link, epee_bois, armure_bois)






# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre de jeu
largeur_fenetre, hauteur_fenetre = 1500, 800
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu ")
liste_region=["interface/foret.png", "interface/montagne.png","interface/desert.png","interface/plage.png","interface/espace.png","interface/train_dernier_boss.png"]

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
TRANSPARENT_NOIR = (0, 0, 0, 50)  # Noir plus transparent

# Chargement du paysage
region_actuel1=rd.randint(0,4)
nombre_de_scene=1
fond_image = pygame.image.load(liste_region[region_actuel1]).convert()
fond_image = pygame.transform.scale(fond_image, (largeur_fenetre, hauteur_fenetre))  # Redimensionne l'image au format de la fenêtre
# Chargement d'images du personnage
personnage_image = pygame.image.load("interface/personnage.png").convert_alpha()  # Charge avec transparence si image PNG
personnage_rect = personnage_image.get_rect(center=(100, 450))  # On place le personnage au départ, à gauche

# Chargement de l'image du monstre
monstre_image = pygame.image.load("interface/monstre.png").convert_alpha()  # Remplace par l'image de ton monstre
monstre_image = pygame.transform.scale(monstre_image, (personnage_image.get_width(), personnage_image.get_height()))  # Mise à l'échelle
monstre_rect = None  # Rectangle du monstre (sera défini lors de l'apparition)

# Variables du joueur
distance_parcourue = 0

# Variables pour le combat
monstre_apparu = False  # Indique si un monstre est présent

distance_monstre = rd.randint(50, 300)

# Fonction pour afficher les stats
def afficher_stats_joueur(joueur):
    font = pygame.font.Font(None, 28)
    # Liste des lignes à afficher
    stats_joueur = [
        f"Nom: {joueur.get_nom()}",
        f"PV: {joueur.get_pv()}/{Link.get_pvmax()}",
        f"Attaque: {joueur.get_attaque()}",
        f"Defense: {joueur.get_defense()}",
        f"Niveau: {joueur.get_niv()}: {joueur.get_exp()}/{joueur.get_niv() * 2}",
        f"Argent: {joueur.get_argent()}",
        f"Arme: {joueur.get_arme().get_nom()}",
        f"Armure: {joueur.get_armure().get_nom()}",
        f"Distance: {distance_parcourue}"
    ]

    # Dessiner un fond noir transparent pour les statistiques joueur
    rect_width = max(font.size(line)[0] for line in stats_joueur) + 20
    rect_height = (font.get_height() + 10) * len(stats_joueur)  # Hauteur basée sur le nombre de lignes
    pygame.draw.rect(fenetre, TRANSPARENT_NOIR, (10, 10, rect_width, rect_height))  # Rectangle noir transparent

    # Afficher chaque ligne joueur
    for index, line in enumerate(stats_joueur):
        text_surface = font.render(line, True, BLANC)
        fenetre.blit(text_surface, (15, 15 + index * (font.get_height() + 5)))  # Positionner chaque ligne

def afficher_stats_creature(creature):
    font = pygame.font.Font(None, 28)
    # Liste des lignes à afficher
    stats_creature = [
        f"Nom: {creature.get_nom()}",
        f"PV: {creature.get_pv()}/{creature.get_pvmax()}",
        f"Attaque: {creature.get_attaque()}",
        f"Defense: {creature.get_defense()}",
        f"Niveau: {creature.get_niv()}",
        f"Argent: {creature.get_butin().get_argent()}",
        f"Arme: {creature.get_arme().get_nom()}",
        f"Armure: {creature.get_armure().get_nom()}"
    ]

    # Dessiner un fond noir transparent pour les statistiques créature
    rect_width = max(font.size(line)[0] for line in stats_creature) + 20
    rect_height = (font.get_height() + 10) * len(stats_creature)  # Hauteur basée sur le nombre de lignes
    pygame.draw.rect(fenetre, TRANSPARENT_NOIR, (1300, 10, rect_width, rect_height))  # Rectangle noir transparent

    # Afficher chaque ligne
    for index, line in enumerate(stats_creature):
        text_surface = font.render(line, True, BLANC)
        fenetre.blit(text_surface, (1300, 10 + index * (font.get_height() + 5)))  # Positionner chaque ligne


# Fonction pour augmenter la distance parcourue
def avancer():
    global distance_parcourue
    distance_parcourue += 1

# Fonction pour créer et gérer les boutons
def bouton(texte, x, y, action=None):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(texte, True, NOIR)  # Texte en noir
    rect = text_surface.get_rect(center=(x + 75, y + 20))  # Centrer le texte dans le bouton

    # Vérifier si la souris est sur le bouton et si on clique
    pygame.draw.rect(fenetre, BLANC, (x, y, 150, 40))  # Dessiner le bouton en blanc
    fenetre.blit(text_surface, rect.topleft)  # Afficher le texte sur le bouton

    souris = pygame.mouse.get_pos()  # Obtenir la position de la souris
    clic = pygame.mouse.get_pressed()  # Obtenir l'état des boutons de la souris

    if rect.collidepoint(souris):
        if clic[0] == 1 and action is not None:
            action()  # Exécuter l'action liée au bouton

# Exemple de fonction à lier aux boutons
def attaquer(joueur, creature):
    global monstre_apparu, en_jeu

    print(f"{joueur.get_nom()}({joueur.get_pv()}/{joueur.get_pvmax()})")
    print(f"{creature.get_nom()}({creature.get_pv()}/{creature.get_pvmax()})")
    joueur_attaque_creature(creature, joueur)
    creature_attaque_joueur(joueur, creature)

    if creature.get_pv() <= 0:
        gagner(joueur, creature)
        joueur.set_pv(min(joueur.get_pvmax(), joueur.get_pv() + joueur.get_pvmax() / 2))
        monstre_apparu = False
        monstre_rect = None
    if joueur.get_pv()<=0:
        en_jeu=False

def fuir():
    global monstre_apparu
    print("Fuite réussie!")
    monstre_apparu = False  # Après la fuite, le monstre disparaît
    monstre_rect = None

# Fonction pour générer un monstre
def generer_monstre():
    global monstre_apparu, monstre_rect, distance_monstre

    monstre_apparu = True
    monstre_rect = monstre_image.get_rect(center=(personnage_rect.right + 50, personnage_rect.centery))  # Juste devant le personnage
    distance_monstre += rd.randint(50, 300)

    return generer_slime(rd.randint(min(1, Link.get_niv()-2), Link.get_niv()+2))
    
# Boucle du jeu
clock = pygame.time.Clock()
en_jeu = True

current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes
Slimy = generer_monstre()
monstre_apparu = False

def aux():
    attaquer(Link, Slimy)
    time.sleep(0.2)

while en_jeu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_jeu = False

    # Gestion des touches (déplacement uniquement vers la droite)
    touches = pygame.key.get_pressed()
    
    # Empêcher le mouvement si un monstre est présent
    if not monstre_apparu and touches[pygame.K_RIGHT]:
        personnage_rect.x += 5  # Déplacement vers la droite
        avancer()  # Augmenter la distance

        # Vérifier si le personnage sort de l'écran
        # Vérifier si le personnage sort de l'écran
        if personnage_rect.x > largeur_fenetre:
            personnage_rect.x = 0  # Remettre le personnage au point de départ (à gauche)
            region_actuel2=rd.randint(0,3)
            while (region_actuel2==region_actuel1):
                region_actuel2=rd.randint(0,3)
            region_actuel1=region_actuel2
            nombre_de_scene+=1
            fond_image = pygame.image.load(liste_region[region_actuel1]).convert()
            fond_image = pygame.transform.scale(fond_image, (largeur_fenetre, hauteur_fenetre)) 

        if nombre_de_scene>=4:
            fond_image = pygame.image.load(liste_region[5]).convert()
            fond_image = pygame.transform.scale(fond_image, (largeur_fenetre, hauteur_fenetre)) 


    # Générer un monstre
    current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes
    if not monstre_apparu and distance_parcourue >= distance_monstre:
        Slimy = generer_monstre()

    # Affichage du fond d'écran
    fenetre.blit(fond_image, (0, 0))
    
    # Affichage des stats
    afficher_stats_joueur(Link)

    # Affichage du personnage
    fenetre.blit(personnage_image, personnage_rect)

    # Affichage des stats du monstre et de l'image du monstre si un monstre est présent
    if monstre_apparu and monstre_rect is not None:
        fenetre.blit(monstre_image, monstre_rect)  # Afficher le monstre
        afficher_stats_creature(Slimy)  # Afficher les stats du monstre

        # Calculer les positions pour centrer les boutons
        bouton_attaque_x = (largeur_fenetre // 2) - (150 // 2)
        bouton_attaque_y = (hauteur_fenetre // 2) - (40 // 2)
        bouton_fuir_x = (largeur_fenetre // 2) - (150 // 2)
        bouton_fuir_y = bouton_attaque_y + 50  # Espace entre les boutons

        # Afficher les boutons "Attaquer" et "Fuir"
        bouton("Attaquer", bouton_attaque_x, bouton_attaque_y, aux)
        bouton("Fuir", bouton_fuir_x, bouton_fuir_y, fuir)

    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)  # Jeu à 60 FPS

# Quitter Pygame
pygame.quit()
