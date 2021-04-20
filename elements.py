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


def move_rhomb(event):
    global setsLists
    print(event)
    move(setsLists[0])
    print(setsLists[0].get('rhomb'))


def move(sets):
    global dx, dy
    #x, y = sets.get('rhomb')[0], sets.get('rhomb')[1]  # === les coordonés x,y du losange
    trajectory = getTrajectory(sets)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcour les trajectoires possible
        print('Boucle ', i, trajectory[i], trajectory[i+1])
        dx,dy=0,0
        x, y = trajectory[i][0], trajectory[i][1]
        mouvement(trajectory[i], trajectory[i+1], x, y)
        

def mouvement(a, b, x, y):
    global dx, dy
    # on vérifie si xi=xi+1
    print('mouvement')
    
    if a[0] / b[0] == 1:
        # Mvt suivant l'axe des ordonnees, vertical
        if y <= b[1]:
            dx = 0
            dy = 1
        else:
            dx = 0
            dy = -1

    if a[1] / b[1] == 1:
        # Mvt suivant l'axe des abcisses, horizontal
        if x <= b[0]:
            dx = 1
            dy = 0
        else:
            dx = -1
            dy = 0
    x = x+(dx*10)
    y = y+(dy*10)
    can.coords(sets.get('rhomb_id')[0],
               x-RADUIS, y,
               x, y-RADUIS,
               x+RADUIS, y,
               x, y+RADUIS
               )
    print("x, y = ", x,y)
    if x != b[0] or y != b[1]:
        fen.after(10, mouvement(a, b, x, y))


# --------------------------Consts--------------------------
RADUIS = 30  # Rayon du losange
dx, dy = 0, 0

fen = Tk()
can = Canvas(fen, width=1000, height=800, bg="yellow")
can.tag_click = True
can.pack(padx=5, pady=5)


#TEST
#allTrajectories = getAllTrajectories(setsLists)
#print(len(allTrajectories), allTrajectories)

'''print(overlaps(
        elementsDictionnary([15,15], [[30,30], [500,30], [500,400], [300,400]], [330, 400], create_rhomb(can, 15,15, RADUIS)),
        elementsDictionnary([400,15], [[400,45], [700,45], [700,145]], [700, 175], create_rhomb(can, 400,15, RADUIS))
    ))
'''
setsLists = [
    elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [700, 500]], [700, 500], create_rhomb(can, 400, 100, RADUIS))
]
for sets in setsLists:
    create_trajectory(can, sets.get('trajectory'))
    create_nosh(can, sets.get('nosh')[0], sets.get('nosh')[1])
    can.tag_bind(sets.get('rhomb_id')[0], '<Button-1>', move_rhomb)
    #can.tag_bind(sets.get('rhomb_id')[1], '<Button-1>', move_rhomb)


fen.mainloop()