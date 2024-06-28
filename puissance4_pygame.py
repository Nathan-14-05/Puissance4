import pygame
from sys import exit

# Initialisation de pygame et création de la fenêtre
pygame.init()
largeurEcran = 700
hauteurEcran = 800
fenetre = pygame.display.set_mode((largeurEcran, hauteurEcran))
pygame.display.set_caption("Puissance 4")

# Variables pour le jeu
largeurEmplacement = 100
police = pygame.font.SysFont("arial", 50)
police2 = pygame.font.SysFont("arial", 40)
police3 = pygame.font.SysFont("arial", 32)

bleu = (91, 80, 196)
lavande = (153, 153, 255)
rouge = (215, 38, 38)
jaune = (222, 182, 25)
blanc = (255, 255, 255)
noir = (0, 0, 0)
rayon = 40.0


# Fonctions
def creationGrillePygame():  # Création de la grille
    grille = [[" " for j in range(7)] for i in range(6)]
    return grille


def affichageGrille(grille, fenetre):
    for l in range(6):
        for c in range(
                7):  # Pour chaque emplacement, on affiche un rectangle bleu avec un cercle de couleur en son centre
            pygame.draw.rect(fenetre, bleu, (
            c * largeurEmplacement, l * largeurEmplacement + largeurEmplacement, largeurEmplacement,
            largeurEmplacement))
            if grille[l][c] == " ":
                pygame.draw.circle(fenetre, blanc, (c * largeurEmplacement + largeurEmplacement / 2,
                                                    l * largeurEmplacement + largeurEmplacement + largeurEmplacement / 2),
                                   rayon)
            elif grille[l][c] == "J":
                pygame.draw.circle(fenetre, jaune, (c * largeurEmplacement + largeurEmplacement / 2,
                                                    l * largeurEmplacement + largeurEmplacement + largeurEmplacement / 2),
                                   rayon)
            elif grille[l][c] == "R":
                pygame.draw.circle(fenetre, rouge, (c * largeurEmplacement + largeurEmplacement / 2,
                                                    l * largeurEmplacement + largeurEmplacement + largeurEmplacement / 2),
                                   rayon)


def placerPion(grille, colonne, couleur,
               compteurTour):  # Vérification des lignes pour trouver la première qui peut accueillir un pion pour une colonne donnée
    ligne = 5
    if 0 <= colonne <= 6:
        while ligne >= 0:
            if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = couleur
                return (ligne, colonne)
            elif grille[ligne][colonne] != " ":
                ligne -= 1
        if ligne < 0:
            compteurTour -= 1
            print("La colonne est déjà pleine !")
            return False


def victoireHorizontale(grille: list, l: int, c: int):
    victoireH = False
    if 0 <= c <= 6:  # On vérifie que la valeur de c n'est pas en dehors du tableau
        if c + 3 <= 6 and grille[l][c] == grille[l][c + 1] == grille[l][c + 2] == grille[l][c + 3]:
            victoireH = True
        elif c - 3 >= 0 and grille[l][c] == grille[l][c - 1] == grille[l][c - 2] == grille[l][c - 3]:
            victoireH = True
    return victoireH


def victoireVerticale(grille: list, l: int, c: int):
    victoireV = False
    if 0 <= l <= 5:  # On vérifie que la valeur de l n'est pas en dehors du tableau
        if l + 3 <= 5 and grille[l][c] == grille[l + 1][c] == grille[l + 2][c] == grille[l + 3][c]:
            victoireV = True
        elif l - 3 >= 0 and grille[l][c] == grille[l - 1][c] == grille[l - 2][c] == grille[l - 3][c]:
            victoireV = True
    return victoireV


def victoireDiagonale(grille: list, l: int, c: int):
    victoireD = False
    if 0 <= l <= 5 and 0 <= c <= 6:  # On vérifie que la valeur de l et c ne sont pas en dehors du tableau
        if l + 3 <= 5 and c + 3 <= 6 and grille[l][c] == grille[l + 1][c + 1] == grille[l + 2][c + 2] == grille[l + 3][
            c + 3]:
            victoireD = True
        elif l + 3 <= 5 and c - 3 >= 0 and grille[l][c] == grille[l + 1][c - 1] == grille[l + 2][c - 2] == \
                grille[l + 3][c - 3]:
            victoireD = True
        elif l - 3 >= 0 and c + 3 <= 6 and grille[l][c] == grille[l - 1][c + 1] == grille[l - 2][c + 2] == \
                grille[l - 3][c + 3]:
            victoireD = True
        elif l - 3 >= 0 and c - 3 >= 0 and grille[l][c] == grille[l - 1][c - 1] == grille[l - 2][c - 2] == \
                grille[l - 3][c - 3]:
            victoireD = True
    return victoireD


def verifVictoire(grille: list, l: int, c: int):  # Toutes les conditions de victoire sont vérifiées
    return victoireHorizontale(grille, l, c) or victoireVerticale(grille, l, c) or victoireDiagonale(grille, l, c)


#########################################################################################################################

# Définition des fonctions qui déterminent l'état actuel du jeu (Menu, jeu en cours, jeu terminé)
def affichageMenu():
    fenetre.fill(lavande)
    titre = police.render("Puissance 4", True, (blanc))
    texte = police2.render("Appuyez sur ESPACE pour commencer", True, (blanc))
    fenetre.blit(titre, (largeurEcran / 2 - titre.get_width() / 2, hauteurEcran / 4))
    fenetre.blit(texte, (largeurEcran / 2 - texte.get_width() / 2, hauteurEcran / 2))

    pygame.display.update()


def affichageJeuFini():
    fenetre.fill(lavande)
    titre = police.render("Partie terminée ! " + joueurActuel + " a gagné !", True, (blanc))
    recommencer = police.render("R - Recommencer", True, (blanc))
    quitter = police.render("Q - Quitter", True, (blanc))
    fenetre.blit(titre, (largeurEcran / 2 - titre.get_width() / 2, hauteurEcran / 2 - titre.get_width() / 3))
    fenetre.blit(recommencer,
                 (largeurEcran / 2 - recommencer.get_width() / 2, hauteurEcran / 1.9 + recommencer.get_height()))
    fenetre.blit(quitter, (largeurEcran / 2 - quitter.get_width() / 2, hauteurEcran / 2 + quitter.get_height() / 2))
    pygame.display.update()


def affichageJeuEgal():
    fenetre.fill(lavande)
    titre = police.render("Partie terminée ! Personne n'a gagné !", True, (blanc))
    recommencer = police.render("R - Recommencer", True, (blanc))
    quitter = police.render("Q - Quitter", True, (blanc))
    fenetre.blit(titre, (largeurEcran / 2 - titre.get_width() / 2, hauteurEcran / 2 - titre.get_width() / 3))
    fenetre.blit(recommencer,
                 (largeurEcran / 2 - recommencer.get_width() / 2, hauteurEcran / 1.9 + recommencer.get_height()))
    fenetre.blit(quitter, (largeurEcran / 2 - quitter.get_width() / 2, hauteurEcran / 2 + quitter.get_height() / 2))
    pygame.display.update()


################################################################

# Autres variables utiles pour le jeu
joueurJaune = str(input("Nom du premier joueur > "))
joueurRouge = str(input("Nom du deuxième joueur > "))
clock = pygame.time.Clock()
etatJeu = "menu"

run = True

# Boucle du jeu
while run:
    clock.tick(40)

    if etatJeu == "menu":  # Par défaut, on affiche le menu
        affichageMenu()
        grille = creationGrillePygame()  # Et on réinitialise la grille à chaque fois, pour recommencer de 0
        compteurTour = 0
        victoire = False  # Tout comme la variable victoire et le compteur de tours
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # On lance le jeu si on appuie sur espace
            etatJeu = "jeuEnCours"

    elif etatJeu == "jeuFini":
        affichageJeuFini()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            etatJeu = "menu"  # Appuyer sur R nous permet de revenir au menu, et donc de recommencer
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif etatJeu == "égalité":
        affichageJeuEgal()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            etatJeu = "menu"
        if keys[pygame.K_q]:
            pygame.quit()
            quit()

    elif etatJeu == "jeuEnCours":
        fenetre.fill(blanc)
        if compteurTour % 2 == 0:
            couleur = "J"
            couleur2 = jaune
            joueurActuel = joueurJaune
        else:
            couleur = "R"
            couleur2 = rouge
            joueurActuel = joueurRouge

        coordCurseur = pygame.mouse.get_pos()  # On récupère les coordonnées du curseur
        pygame.draw.circle(fenetre, couleur2, (coordCurseur[0], 50),
                           rayon)  # Et on affiche le pion par dessus ces coordonnées

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                coordClic = event.pos  # On récupère les coordonnées du clic de la souris
                colonne = coordClic[0] // 100  # On divise par 100 avec un reste pour obtenir la colonne
                coordPion = placerPion(grille, colonne, couleur, compteurTour)
                if coordPion != False:
                    victoire = verifVictoire(grille, coordPion[0], coordPion[1])
                    compteurTour += 1
                    if victoire:
                        etatJeu = "jeuFini"
                    elif compteurTour == 42:
                        etatJeu = "égalité"

                        # Affiche le nom du joueur actuel à l'écran
        text = police2.render("C'est à " + joueurActuel + " de jouer", True, (0, 0, 0))
        fenetre.blit(text, (10, 750))

        affichageGrille(grille, fenetre)
        pygame.display.update()