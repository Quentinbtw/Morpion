grille = [[0,0,0], [0,0,0], [0,0,0]]

def round(grille, x, y, joueur):

    if x < 3 and y < 3 and x > -1 and y > -1 and grille[x][y] == 0:

        grille[x][y] = joueur
        return True
    
    else:
        return False

def end(grille):

    for i in range(len(grille)) :

        if grille[i][0] == grille[i][1] and grille[i][2] == grille[i][0] and grille[i][1] != 0:
            return grille[i][0]
    
        elif grille[0][i] == grille[1][i] and grille[2][i] == grille[0][i] and grille[1][i] != 0:

            return grille[0][i]

    if grille[0][2] == grille[1][1] and grille[2][0] == grille[0][2] and grille[2][0] != 0:

        return grille[0][2]

    elif grille[0][0] == grille[1][1] and grille[2][2] == grille[1][1] and grille[1][1] != 0:

        return grille[0][0]
    
    for x in range(len(grille)):
        for y in range(len(grille)):
    
            if grille[x][y] == 0:

                return 0

    return -1

print(" ".join(str(grille[0])))
print(" ".join(str(grille[1])))
print(" ".join(str(grille[2])))

joueur = 1   

while end(grille) == 0:

    print("Au tour du joueur "+str(joueur))

    x = int(input("Sur quelle ligne voulez-vous jouer ??? "))
    y = int(input("Sur quelle colonne voulez-vous jouer ??? "))

    while not round(grille, x, y, joueur):
        print("La case est déja prise ou pas dans la grille, merci de bouger.")
        x = int(input("Sur quelle ligne voulez-vous jouer ??? "))
        y = int(input("Sur quelle colonne voulez-vous jouer ??? "))


    print(" ".join(str(grille[0])))
    print(" ".join(str(grille[1])))
    print(" ".join(str(grille[2])))

    if joueur == 1:
        joueur = 2 

    elif joueur == 2:
        joueur = 1

gagnant = end(grille)
if gagnant == -1:
    print("Pas de gagnant, redémarrez la partie ")
else :
    print("Le joueur "+str(gagnant)+" a gagné ! Bravo !")