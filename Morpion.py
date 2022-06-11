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

def jouer(grille, x, y, boutons, game, score0, score1) :

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
        photo = PhotoImage(file = "./croix.PNG")
        

    elif joueur == 2 and reply:
        photo = PhotoImage(file = "./rond.PNG")

    boutons[3 * x + y].configure(image=photo)
    boutons[3 * x + y].photo = photo

    gagnant = end(grille)

    if gagnant == 0:
        return

    elif gagnant == -1:
        
        game = (game + 1)% 2

        for widget in window.winfo_children():
            widget.destroy()

        text_gagnant = Label(window, text = "Bizzare")
        text_gagnant.pack()

        text_score = Label(window, text = "Louis -  "+str(score0)+" : "+str(score1)+"  - Quentin" )
        text_score.pack()

        btn = Button(window, text ="Recommencer", command = lambda : begin(game, score0, score1))
        btn.pack()

    else:

        game =(game + 1)% 2

        if (game + gagnant) % 2 == 0:
            score0 += 1

        else : 
            score1 += 1

        for widget in window.winfo_children():
            widget.destroy()

        text_gagnant = Label(window, text = "Le gagnant c le : "+str(gagnant))
        text_gagnant.pack()

        text_score = Label(window, text = "Louis -  "+str(score0)+" : "+str(score1)+"  - Quentin" )
        text_score.pack()

        btn = Button(window, text ="Recommencer", command = lambda : begin(game, score0, score1))
        btn.pack()

def begin(game, score0, score1) :

    for widget in window.winfo_children():
            widget.destroy()

    WIDTH = 250
    HEIGHT = 250
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    H_MARGIN = int((screen_height - 3 * HEIGHT) / 2)
    W_MARGIN = int((screen_width - 3 * WIDTH) / 2)
    
    photo = PhotoImage(file = "./vide.PNG")

    btn11 = Button(window, image = photo, command = lambda : jouer(grille, 0, 0, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn11.image = photo
    btn11.place(x = W_MARGIN, y = H_MARGIN)

    btn12 = Button(window, image = photo, command = lambda : jouer(grille, 0, 1, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn12.place(x = W_MARGIN + WIDTH, y = H_MARGIN)

    btn13 = Button(window, image = photo, command = lambda : jouer(grille, 0, 2, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn13.place(x = W_MARGIN + WIDTH*2, y = H_MARGIN)

    btn21 = Button(window, image = photo, command = lambda : jouer(grille, 1, 0, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn21.place(x = W_MARGIN, y = H_MARGIN + HEIGHT)

    btn22 = Button(window, image = photo, command = lambda : jouer(grille, 1, 1, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn22.place(x = W_MARGIN + WIDTH, y = H_MARGIN + HEIGHT)

    btn23 = Button(window, image = photo, command = lambda : jouer(grille, 1, 2, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn23.place(x = W_MARGIN + WIDTH*2, y = H_MARGIN +HEIGHT)

    btn31 = Button(window, image = photo, command = lambda : jouer(grille, 2, 0, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn31.place(x = W_MARGIN, y = H_MARGIN + HEIGHT*2)

    btn32 = Button(window, image = photo, command = lambda : jouer(grille, 2, 1, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn32.place(x = W_MARGIN + WIDTH, y = H_MARGIN + HEIGHT*2)

    btn33 = Button(window, image = photo, command = lambda : jouer(grille, 2, 2, boutons, game, score0, score1), height = HEIGHT, width = WIDTH)
    btn33.place(x = W_MARGIN + WIDTH*2, y = H_MARGIN + HEIGHT*2)

    boutons = [btn11, btn12, btn13, btn21, btn22, btn23, btn31, btn32, btn33]

    grille = [[0,0,0], [0,0,0], [0,0,0]]

window = Tk()
window.attributes('-fullscreen', True) 

game = 0
score0 = 0
score1 = 0

begin(game, score0, score1)

window.mainloop()