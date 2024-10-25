import pygame
import random as rd

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

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre de jeu
largeur_fenetre, hauteur_fenetre = 800, 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu ")

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
TRANSPARENT_NOIR = (0, 0, 0, 180)  # Noir plus transparent

# Chargement du paysage
fond_image = pygame.image.load("interface/foret.png").convert()
fond_image = pygame.transform.scale(fond_image, (largeur_fenetre, hauteur_fenetre))  # Redimensionne l'image au format de la fenêtre

# Chargement d'images du personnage
personnage_image = pygame.image.load("interface/personnage.png").convert_alpha()  # Charge avec transparence si image PNG
personnage_rect = personnage_image.get_rect(center=(100, 300))  # On place le personnage au départ, à gauche

# Chargement de l'image du monstre
monstre_image = pygame.image.load("interface/monstre.png").convert_alpha()  # Remplace par l'image de ton monstre
monstre_image = pygame.transform.scale(monstre_image, (personnage_image.get_width(), personnage_image.get_height()))  # Mise à l'échelle
monstre_rect = None  # Rectangle du monstre (sera défini lors de l'apparition)

# Variables du joueur
pv = 100
pv_max = 100
attaque = 20
defense = 5
niveau = 1
argent = 50
arme_equipee = "Épée en bois"
armure_equipee = "Armure légère"
distance_parcourue = 0

# Variables pour le combat
monstre_apparu = False  # Indique si un monstre est présent
monstre_pv = 50  # Points de vie du monstre
monstre_niveau = 1  # Niveau du monstre

# Variables pour le timer du monstre
monstre_timer = 0  # Compteur de temps
intervalle_appearance = 10000  # Intervalle d'apparition du monstre en millisecondes

# Fonction pour afficher les stats
def afficher_stats():
    font = pygame.font.Font(None, 28)
    # Liste des lignes à afficher
    stats_lines = [
        f"PV: {pv}/{pv_max}",
        f"Attaque: {attaque}",
        f"Défense: {defense}",
        f"Niveau: {niveau}",
        f"Argent: {argent}",
        f"Arme: {arme_equipee}",
        f"Armure: {armure_equipee}",
        f"Distance: {distance_parcourue}"
    ]

    # Dessiner un fond noir transparent pour les statistiques
    rect_width = max(font.size(line)[0] for line in stats_lines) + 20
    rect_height = (font.get_height() + 10) * len(stats_lines)  # Hauteur basée sur le nombre de lignes
    pygame.draw.rect(fenetre, TRANSPARENT_NOIR, (10, 10, rect_width, rect_height))  # Rectangle noir transparent

    # Afficher chaque ligne
    for index, line in enumerate(stats_lines):
        text_surface = font.render(line, True, BLANC)
        fenetre.blit(text_surface, (15, 15 + index * (font.get_height() + 5)))  # Positionner chaque ligne

# Fonction pour afficher les stats du monstre
def afficher_stats_monstre():
    if monstre_rect is not None:
        font = pygame.font.Font(None, 24)
        stats_monstre_text = f"Niveau: {monstre_niveau} | PV: {monstre_pv}"

        # Positionner le texte juste au-dessus du monstre
        text_surface = font.render(stats_monstre_text, True, NOIR)  # Texte en noir
        text_rect = text_surface.get_rect(center=(monstre_rect.centerx, monstre_rect.top - 15))

        # Afficher le texte
        fenetre.blit(text_surface, text_rect.topleft)

# Fonction pour augmenter la distance parcourue
def avancer():
    global distance_parcourue
    distance_parcourue += rd.randint(1, 5)

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
def attaquer():
    global monstre_apparu, monstre_pv
    print("Attaque réussie!")
    monstre_pv -= attaque  # Soustraire les dégâts du monstre

    if monstre_pv <= 0:  # Si le monstre est vaincu
        print("Monstre vaincu!")
        reset_monstre()

def fuir():
    global monstre_apparu
    print("Fuite réussie!")
    monstre_apparu = False  # Après la fuite, le monstre disparaît
    reset_monstre()  # Réinitialise les valeurs du monstre

def reset_monstre():
    global monstre_apparu, monstre_rect, monstre_pv, monstre_niveau
    monstre_apparu = False
    monstre_rect = None  # Réinitialiser le rectangle du monstre
    monstre_pv = 50  # Réinitialiser les PV du monstre
    monstre_niveau = 1  # Réinitialiser le niveau du monstre

# Fonction pour générer un monstre
def generer_monstre():
    global monstre_apparu, monstre_rect, monstre_pv, monstre_niveau, monstre_timer
    current_time = pygame.time.get_ticks()  # Temps actuel en millisecondes

    # Vérifier si le monstre est déjà apparu
    if not monstre_apparu and (current_time - monstre_timer > intervalle_appearance):
        monstre_apparu = True
        monstre_rect = monstre_image.get_rect(center=(personnage_rect.right + 50, personnage_rect.centery))  # Juste devant le personnage
        monstre_timer = current_time  # Réinitialiser le timer

# Boucle du jeu
clock = pygame.time.Clock()
en_jeu = True

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
        if personnage_rect.x > largeur_fenetre:
            personnage_rect.x = 0  # Remettre le personnage au point de départ (à gauche)

    # Générer un monstre
    generer_monstre()

    # Affichage du fond d'écran
    fenetre.blit(fond_image, (0, 0))

    # Affichage des stats
    afficher_stats()

    # Affichage du personnage
    fenetre.blit(personnage_image, personnage_rect)

    # Affichage des stats du monstre et de l'image du monstre si un monstre est présent
    if monstre_apparu and monstre_rect is not None:
        fenetre.blit(monstre_image, monstre_rect)  # Afficher le monstre
        afficher_stats_monstre()  # Afficher les stats du monstre

        # Calculer les positions pour centrer les boutons
        bouton_attaque_x = (largeur_fenetre // 2) - (150 // 2)
        bouton_attaque_y = (hauteur_fenetre // 2) - (40 // 2)
        bouton_fuir_x = (largeur_fenetre // 2) - (150 // 2)
        bouton_fuir_y = bouton_attaque_y + 50  # Espace entre les boutons

        # Afficher les boutons "Attaquer" et "Fuir"
        bouton("Attaquer", bouton_attaque_x, bouton_attaque_y, attaquer)
        bouton("Fuir", bouton_fuir_x, bouton_fuir_y, fuir)

    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)  # Jeu à 60 FPS

# Quitter Pygame
pygame.quit()
