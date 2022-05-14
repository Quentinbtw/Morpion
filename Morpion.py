from tkinter import *  

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

def jouer(grille, x, y, boutons) :

    compteur = 0

    for x1 in range(len(grille)) :
        for y1 in range(len(grille[x])) :
            if grille[x1][y1] == 0:
                compteur += 1
    
    if compteur % 2 == 1 :
        joueur = 1
    else :
        joueur = 2

    reply = round(grille, x, y, joueur)

    if joueur == 1 and reply:
        boutons[3 * x + y]['text'] = 'X'

    elif joueur == 2 and reply:
        boutons[3 * x + y]['text'] = 'O'

    gagnant = end(grille)

    if gagnant == 0:
        return

    elif gagnant == -1:

        for widget in window.winfo_children():
            widget.destroy()

        text_gagnant = Label(window, text = "Bizzare")
        text_gagnant.pack()

        btn = Button(window, text ="Recommencer", command = begin)
        btn.pack()

    else:

        for widget in window.winfo_children():
            widget.destroy()

        text_gagnant = Label(window, text = "Le gagnant c le : "+str(gagnant))
        text_gagnant.pack()

        btn = Button(window, text ="Recommencer", command = begin)
        btn.pack()

def begin() :

    for widget in window.winfo_children():
            widget.destroy()

    btn11 = Button(window, text =" ", command = lambda : jouer(grille, 0, 0, boutons), height = 15, width = 20)
    btn11.grid(row = 0, column = 0)

    btn12 = Button(window, text =" ", command = lambda : jouer(grille, 0, 1, boutons), height = 15, width = 20)
    btn12.grid(row = 0, column = 1)

    btn13 = Button(window, text =" ", command = lambda : jouer(grille, 0, 2, boutons), height = 15, width = 20)
    btn13.grid(row = 0, column = 2)

    btn21 = Button(window, text =" ", command = lambda : jouer(grille, 1, 0, boutons), height = 15, width = 20)
    btn21.grid(row = 1, column = 0)

    btn22 = Button(window, text =" ", command = lambda : jouer(grille, 1, 1, boutons), height = 15, width = 20)
    btn22.grid(row = 1, column = 1)

    btn23 = Button(window, text =" ", command = lambda : jouer(grille, 1, 2, boutons), height = 15, width = 20)
    btn23.grid(row = 1, column = 2)

    btn31 = Button(window, text =" ", command = lambda : jouer(grille, 2, 0, boutons), height = 15, width = 20)
    btn31.grid(row = 2, column = 0)

    btn32 = Button(window, text =" ", command = lambda : jouer(grille, 2, 1, boutons), height = 15, width = 20)
    btn32.grid(row = 2, column = 1)

    btn33 = Button(window, text =" ", command = lambda : jouer(grille, 2, 2, boutons), height = 15, width = 20)
    btn33.grid(row = 2, column = 2)

    boutons = [btn11, btn12, btn13, btn21, btn22, btn23, btn31, btn32, btn33]

    grille = [[0,0,0], [0,0,0], [0,0,0]]

window = Tk()
window.attributes('-fullscreen', True) 

begin()

window.mainloop()