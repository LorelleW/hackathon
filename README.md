<h1> Lign attak </h1>

<h3> Introduction </h3>

<h4> Le projet à été réalisé par une équipe de 5 ING1 et supervisée par 2 ING2 dans le cadre
d'un hackaton de 36h, le but étant de faire travailler les structures de données.
Le parti pris de l'équipe à été de consacrer une partie du temps donné à la réalisation
et l'implémentation de graphismes réalisés en ASCII Art pour un style minimaliste et unique.
Le style du jeu est un roguelike </h4>


<h3>  Gameplay </h3>

<h4> Le gameplay du jeu consiste à avancer sur une ligne droite
à travers plusieurs biomes. A chaque pas, une rencontre avec un monstre est possible, à ce moment,
un combat s'enclenche. La mécanique de combat est le coeur du gameplay : le joueur, dépendamment des informations
qu'il a sur le héros et sur le monstre, peut évaluer la situation avant de choisir entre une option entre la fuite, l'attaque ou l'utilisation d'une compétence. Chaque attaque sera
suivie d'une réponse de l'ennemi. Si le monstre est tué, il peut drop un ou plusieurs points d'exp
et éventuellement son stuff si il en a un. Chaque kill heal le joueur de la moitié de ses HP max.</h4>

<h3> Contrôles </h3>

<h4> Les contrôles sont assez rudimentaires, flêche de droite, pour aller à droite,
click gauche sur les différents boutons pour effectuer leur actions (attaquer ect...).
Le joueur peut aussi à tout moment consulter son inventaire</h4>

<h3> Contexte</h3>

<h4> Le jeu ayant été réalisé dans un temps très court, plusieurs éléments n'ont
pas pu être implémentés. Des éléments comme les marchands, la rareté des objets
la diversité des biomes ... sont présents dans le code mais n'ont pas pu être implémentés
dans la version finale</h4>

<h3> Setup </h3>

<h4> Pour setup le jeu il suffit de cloner le dépôt.
La seule bibliothèque à installer au préalable est Pygame, pour l'installer : 
pip install pygame
Pour run le jeu, simplement lancer jeutest.py</h4>
