#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:49:46 2021

@author: alberic
"""

from tkinter import *
from math import *

# --------------------------Fonctions de creation d'elements graphiques--------------------------

# Creer un rhomb


def create_rhomb(canvas, x, y, raduis=30):
    r1 = canvas.create_polygon(x-raduis, y,
                               x, y-raduis,
                               x+raduis, y,
                               x, y+raduis,
                               fill="#4389fe")
    r2 = canvas.create_polygon(x-(raduis-15), y,
                               x, y-(raduis-15),
                               x+(raduis-15), y,
                               x, y+(raduis-15),
                               fill="#1875d1")
    return [r1, r2]


def create_stick(canvas, debut, end):
    return canvas.create_line(debut[0], debut[1], end[0], end[1], fill="#1875d1", width=3)


def create_trajectory(canvas, trajectory_coordinates):
    coul = "#1875d1"
    for i in range(len(trajectory_coordinates)-1):
        canvas.create_line(trajectory_coordinates[i][0],
                           trajectory_coordinates[i][1],
                           trajectory_coordinates[i+1][0],
                           trajectory_coordinates[i+1][1],
                           fill=coul,
                           width=3
                           )


def create_nosh(canvas, x, y, raduis=30):
    nosh = canvas.create_polygon(x-raduis, y,
                                 x, y-raduis,
                                 x+raduis, y,
                                 x, y+raduis,
                                 fill='', outline='#4389fe', width=3)
    return nosh


def elementsDictionnary(rhomb_coordinates, trajectory_coordinates, nosh_coordinates, rhombs_id_list):
    "Permet la creation du dictionnaire contenant tous les elements d'un ensemble"
    # rhomb_coordinates represente les coordonnes du centre d'un losange
    # trajectory_coordinates represente la liste des points qui permettront la creation de la trajectoire
    # nosh_coordinates represente les coordonnes du centre de l'encoche
    # rhomb_id_lists est la liste des deux id representant les losanges crees (create_rhomb)
    return {
        'rhomb': rhomb_coordinates,
        'trajectory': trajectory_coordinates,
        'nosh': nosh_coordinates,
        'rhomb_id': rhombs_id_list
    }


def getTrajectory(sets):
    return sets.get("trajectory")


'''
def getAllTrajectories(setsLists):
    allTrajectories = []
    for i in setsLists:
        allTrajectories.append(getTrajectory(i))
    return allTrajectories
'''


def overlaps(firstSet, secondSet):
    "Determine si deux pions (losanges) se chevauchent ou pas"
    # firstSet et secondSet sont des ensembles
    overlaping = False
    i, j = firstSet.get('rhomb'), secondSet.get('rhomb')
    x, y, xprim, yprim = i[0], i[1], j[0], j[1]
    if yprim - y <= RADUIS*2 and xprim - x <= RADUIS * 2:
        print(yprim - y, xprim - x, RADUIS)
        overlaping = True
    return overlaping


'''
def move(sets):
    #sets = ensemble
    x, y = sets.get('rhomb')[0], sets.get('rhomb')[1]
    trajectory = getTrajectory(sets)
    dx, dy = 0, 0
    for i in range(len(trajectory)-1):
        #print(trajectory[i:i+2])
        if trajectory[i][0] / trajectory[i+1][0] == 1:
            #Mvt suivant l'axe des ordonnees
            if y <= trajectory[i+1][1]:
                y, dx, dy = y+(RADUIS*2), dx, RADUIS
        if trajectory[i][1] / trajectory[i+1][1] == 1:
            #Mvt suivant l'axe des abcisses
            if x <= trajectory[i+1][0]:
                x, dx, dy = x+(RADUIS*2), RADUIS, dy
        if trajectory[i][0] / trajectory[i+1][0] != 1 and trajectory[i][1] / trajectory[i+1][1] != 1:
            #Mvt oblique
            x, y, dx, dy = x+(RADUIS*2), y+(RADUIS*2), trajectory[i][0] / trajectory[i+1][0], trajectory[i][1] / trajectory[i+1][1]
        sets.get('rhomb')[0], sets.get('rhomb')[1] = x, y
        
        can.coords(sets.get('rhomb_id')[0],sets.get('rhomb')[0],sets.get('rhomb')[1],sets.get('rhomb')[0]+RADUIS,sets.get('rhomb')[1]+RADUIS)
        can.coords(sets.get('rhomb_id')[1],sets.get('rhomb')[0],sets.get('rhomb')[1],sets.get('rhomb')[0]+RADUIS,sets.get('rhomb')[1]+RADUIS)
    fen.after(20, move(sets))

def move_rhomb(event):
    global setsLists
    for sets in setsLists:
        move(sets)
    
'''
'''
def move():
    global sets
    x, y = sets.get('rhomb')[0], sets.get('rhomb')[1]
    trajectory = getTrajectory(sets)
    dx, dy = 0, 0
    i = 0
    if trajectory[i][0] / trajectory[i+1][0] == 1:
        #Mvt suivant l'axe des ordonnees
        if y <= trajectory[i+1][1]:
            y, dx, dy = y+(RADUIS*2), dx, RADUIS
    if trajectory[i][1] / trajectory[i+1][1] == 1:
        #Mvt suivant l'axe des abcisses
        if x <= trajectory[i+1][0]:
            x, dx, dy = x+(RADUIS*2), RADUIS, dy
    if trajectory[i][0] / trajectory[i+1][0] != 1 and trajectory[i][1] / trajectory[i+1][1] != 1:
        #Mvt oblique
        x, y, dx, dy = x+(RADUIS*2), y+(RADUIS*2), trajectory[i][0] / trajectory[i+1][0], trajectory[i][1] / trajectory[i+1][1]
    sets.get('rhomb')[0], sets.get('rhomb')[1] = x, y
    can.coords(sets.get('rhomb_id')[0],sets.get('rhomb')[0],sets.get('rhomb')[1],sets.get('rhomb')[0]+RADUIS,sets.get('rhomb')[1]+RADUIS)
    can.coords(sets.get('rhomb_id')[1],sets.get('rhomb')[0],sets.get('rhomb')[1],sets.get('rhomb')[0]+RADUIS,sets.get('rhomb')[1]+RADUIS)
    i += 1
    fen.after(20, move)
'''


def move(sets):
    #sets = ensemble
    global dx, dy
    x, y = sets.get('rhomb')[0], sets.get('rhomb')[
        1]  # === les coordonés x,y du losange
    trajectory = getTrajectory(sets)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcour les trajectoires possible
        #print(trajectory[i], trajectory[i+1])
        # break
        dx,dy=0,0
        print('Boucle', i)
        mouvement(trajectory[i], trajectory[i+1], x, y)


def mouvement(a, b, x, y):
    global dx, dy
    # on vérifie si xi=xi+1
    
    if a[0] / b[0] == 1:
        # Mvt suivant l'axe des ordonnees, vertical
        if y <= b[1]:
            #y, dx, dy = y+(RADUIS*2), dx, RADUIS
            dx = 0
            dy = 1
        else:
            dx = 0
            dy = -1

    if a[1] / b[1] == 1:
        # Mvt suivant l'axe des abcisses, horizontal
        if x <= b[0]:
            #x, dx, dy = x+(RADUIS*2), RADUIS, dy
            dx = 1
            dy = 0
        else:
            dx = -1
            dy = 0
    x = x+(dx*10)
    y = y+(dy*10)
    # affecter la ligne de trajectoire

    #x, y, dx, dy = x+(RADUIS*2), y+(RADUIS*2), trajectory[i][0] / trajectory[i+1][0], trajectory[i][1] / trajectory[i+1][1]
    # ne pas affecter le dictionnaire principale???
    sets.get('rhomb')[0], sets.get('rhomb')[1] = x, y
    can.coords(sets.get('rhomb_id')[0],
               x-RADUIS, y,
               x, y-RADUIS,
               x+RADUIS, y,
               x, y+RADUIS
               )
    # can.coords(sets.get('rhomb_id')[0],
    #             x-(RADUIS-15), y,
    #             x, y-(RADUIS-15),
    #             x+(RADUIS-15), y,
    #             x, y+(RADUIS-15)
    #           )   

    if x != b[0] and y != b[1]:
        #print(x, y, a, b)
        print('Recursivite')
        fen.after(10, mouvement(a, b, x, y))


def move_rhomb(event):
    global setsLists
    move(setsLists[0])


# --------------------------Consts--------------------------
RADUIS = 30  # Rayon du losange
dx, dy = 0, 0

fen = Tk()
can = Canvas(fen, width=1000, height=800, bg="yellow")
can.tag_click = True
can.pack(padx=5, pady=5)


# TEST
#allTrajectories = getAllTrajectories(setsLists)
#print(len(allTrajectories), allTrajectories)

'''print(overlaps(
        elementsDictionnary([15,15], [[30,30], [500,30], [500,400], [300,400]], [330, 400], create_rhomb(can, 15,15, RADUIS)),
        elementsDictionnary([400,15], [[400,45], [700,45], [700,145]], [700, 175], create_rhomb(can, 400,15, RADUIS))
    ))
'''
setsLists = [
    elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [
                        700, 500]], [700, 500], create_rhomb(can, 400, 100, RADUIS))
]
for sets in setsLists:
    create_trajectory(can, sets.get('trajectory'))
    create_nosh(can, sets.get('nosh')[0], sets.get('nosh')[1])
    can.tag_bind(sets.get('rhomb_id')[0], '<Button-1>', move_rhomb)
    #can.tag_bind(sets.get('rhomb_id')[1], '<Button-1>', move_rhomb)


fen.mainloop()
