def creerGrille():  # Fonction qui créer la grille
    grille = [[" " for j in range(7)] for i in
              range(6)]  # La grille est composée de 6 listes de 7 valeurs chacune, 6 lignes de 7 colonnes
    return grille  # On renvoie la grille


def affichage(grille: list):  # Fonction qui se charge de l'affichage de la grille
    for l in range(6):  # A chaque ligne, on affiche le contenu ci-dessous
        print("---------------")
        print("", end="|")
        for c in range(
                7):  # Et pour chaque colonne, on affiche la valeur de la grille aux coordonnées l et c (soit ligne et colonne)
            print(grille[l][c], end="|")
        print("")
    print("---------------")


def placerPion(grille: list, colonne: int, couleur: str,
               compteurTour: int):  # Fonction qui sert à trouver la première ligne disponible pour la colonne indiquée par le joueur
    ligne = 5  # On commence à la dernière ligne, soit la 5 ème
    if 0 <= colonne <= 6:  # Cette condition vérifie que le chiffre saisit est entre 0 et 6
        while ligne >= 0:
            if grille[ligne][colonne] == " ":  # Si la case est vide, on peut lui assigner la couleur du joueur actuel
                grille[ligne][colonne] = couleur
                return (ligne, colonne)  # Et on retourne les coordonnées pour vérifier la victoire
            elif grille[ligne][
                colonne] != " ":  # Sinon, on soustrait la ligne par 1. On recommence la vérification pour la ligne d'au dessus
                ligne -= 1
        if ligne < 0:  # Si la variable ligne passe en dessous de 0, celà signifie que la colonne est pleine
            compteurTour -= 1  # On revient donc un tour en arrière
            print("La colonne est déjà pleine !")
            return False  # Et on renvoie False au lieu des coordonnées du pion placé
    else:  # Si le joueur rentre un chiffre qui n'est pas entre 0 et 6, la colonne n'existe pas
        print("Cette colonne n'existe pas !")
        return False  # On renvoie également False


def victoireHorizontale(grille: list, l: int,
                        c: int):  # Cette fonction vérifie si il y a un alignement de 4 pions horizontalement
    victoireH = False
    if 0 <= c <= 6:  # On vérifie que la valeur de c n'est pas en dehors du tableau
        if c + 3 <= 6 and grille[l][c] == grille[l][c + 1] == grille[l][c + 2] == grille[l][c + 3]:
            victoireH = True
        elif c - 3 >= 0 and grille[l][c] == grille[l][c - 1] == grille[l][c - 2] == grille[l][c - 3]:
            victoireH = True
    return victoireH


def victoireVerticale(grille: list, l: int,
                      c: int):  # Cette fonction vérifie si il y a un alignement de 4 pions verticalement
    victoireV = False
    if 0 <= l <= 5:  # On vérifie que la valeur de l n'est pas en dehors du tableau
        if l + 3 <= 5 and grille[l][c] == grille[l + 1][c] == grille[l + 2][c] == grille[l + 3][c]:
            victoireV = True
        elif l - 3 >= 0 and grille[l][c] == grille[l - 1][c] == grille[l - 2][c] == grille[l - 3][c]:
            victoireV = True
    return victoireV


def victoireDiagonale(grille: list, l: int,
                      c: int):  # Cette fonction vérifie si il y a un alignement de 4 pions en diagonale
    victoireD = False
    if 0 <= l <= 5 and 0 <= c <= 6:  # On vérifie que la valeur de l et c n'est pas en dehors du tableau
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


def verifVictoire(grille: list, l: int,
                  c: int):  # Cette fonction appelle les 3 fonctions précedemment crées pour tout vérifier
    return victoireHorizontale(grille, l, c) or victoireVerticale(grille, l, c) or victoireDiagonale(grille, l, c)


def jeu(grille: list):  # Fonction principale
    joueurJaune = str(input("Bonjour ! Veuillez saisir le nom du premier joueur > "))  # On demande le nom des 2 joueurs
    joueurRouge = str(input("Et le nom du deuxième joueur > "))
    compteurTour = 0  # On initialise le compteur de tour à 0
    victoire = False
    while compteurTour < 42 and victoire == False:
        if compteurTour % 2 == 0:
            couleur = "J"
            joueurActuel = joueurJaune
        else:
            couleur = "R"
            joueurActuel = joueurRouge

        colonne = int(input(joueurActuel + " c'est à votre tour ! Choisissez une colonne de 0 à 6 > "))

        coord = placerPion(grille, colonne, couleur, compteurTour)
        if coord != False:
            affichage(grille)
            victoire = verifVictoire(grille, coord[0], coord[1])
            compteurTour += 1

    if compteurTour == 42:
        print("Personne n'a gagné !")

    else:
        print("Partie terminée ! " + joueurActuel + " a gagné !")


if __name__ == '__main__':
    jeu(creerGrille())