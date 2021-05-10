#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:49:46 2021

@author: alberic
"""

from tkinter import *
from math import *
import sys

# --------------------------Fonctions de creation d'elements graphiques--------------------------

# Creer un rhomb


def create_rhomb(canvas, x, y, raduis=30):
    r1 = canvas.create_polygon(x-raduis, y,
                               x, y-raduis,
                               x+raduis, y,
                               x, y+raduis,
                               fill="#4389fe")
    return r1


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


def elementsDictionnary(rhomb_coordinates, trajectory_coordinates, nosh_coordinates, rhomb_id):
    "Permet la creation du dictionnaire contenant tous les elements d'un ensemble"
    # rhomb_coordinates represente les coordonnes du centre d'un losange
    # trajectory_coordinates represente la liste des points qui permettront la creation de la trajectoire
    # nosh_coordinates represente les coordonnes du centre de l'encoche
    # rhomb_id_lists est la liste des deux id representant les losanges crees (create_rhomb)
    return {
        'rhomb': rhomb_coordinates,
        'trajectory': trajectory_coordinates,
        'nosh': nosh_coordinates,
        'rhomb_id': rhomb_id
    }


def getTrajectory(sets):
    return sets.get("trajectory")

def getRhombTag(sets):
    return sets.get("rhomb_id")


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
    global level1, can
    #print('setsLists: ', setsLists)
    for sets in level1:
        print('tag: ', sets.get('rhomb_id'), 'clicked tag: ', event.widget.find_withtag("current"))
        if sets.get('rhomb_id') == event.widget.find_withtag("current")[0]:
            move(sets)
            # can.tag_bind(level1[event.widget.find_withtag("current")[0]].get('rhomb_id'), BUTTON1, move_rhomb)
            break





def move(sets):
    global dx, dy
    print(sets)
    trajectory = getTrajectory(sets)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcour les trajectoires possible
        #print('Boucle ', i, trajectory[i], trajectory[i+1])
        dx,dy=0,0
        x, y = trajectory[i][0], trajectory[i][1]
        mouvement(trajectory[i], trajectory[i+1], x, y, sets)        

def mouvement(a, b, x, y, sets):
    global dx, dy
    # on vérifie si xi=xi+1
    #print('mouvement')
    
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
    can.coords(sets.get('rhomb_id'),
               x-RADUIS, y,
               x, y-RADUIS,
               x+RADUIS, y,
               x, y+RADUIS
               )
    #print("x, y = ", x,y)
    if x != b[0] or y != b[1]:
        fen.after(10, mouvement, a, b, x, y, sets)

def drawlevel(can, level_list):
    for assembly in level_list:
        create_trajectory(can, assembly.get('trajectory'))
        create_nosh(can, assembly.get('nosh')[0], assembly.get('nosh')[1])






# --------------------------Consts--------------------------
RADUIS = 30  # Rayon du losange
dx, dy = 0, 0
BUTTON1 = '<Button-1>'

fen = Tk()
fen.title("RHOMB")
can = Canvas(fen, width=1500, height=800, bg="yellow")
can.pack()


#TEST
'''print(overlaps(
        elementsDictionnary([15,15], [[30,30], [500,30], [500,400], [300,400]], [330, 400], create_rhomb(can, 15,15, RADUIS)),
        elementsDictionnary([400,15], [[400,45], [700,45], [700,145]], [700, 175], create_rhomb(can, 400,15, RADUIS))
    ))
'''
# setsLists = [
#     elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [700, 500]], [700, 500], create_rhomb(can, 400, 100, RADUIS)),
#     elementsDictionnary([120,30], [[120,30], [700,30], [700,300]], [700, 300], create_rhomb(can, 120,30, RADUIS)),
#     #elementsDictionnary([900,400], [[900,400], [400,500], [400,350]], [400, 350], create_rhomb(can, 900,400, RADUIS))
# ]

level1 = [
    {
        'rhomb': [250, 250],
        'trajectory': [[250, 250], [250, 440], [950, 440], [950, 250]],
        'nosh': [950, 250],
        'rhomb_id': create_rhomb(can, 250, 250, RADUIS)
    },
    {
        'rhomb': [350, 250],
        'trajectory': [[350, 250], [350, 400]],
        'nosh': [350, 400],
        'rhomb_id': create_rhomb(can, 350, 250, RADUIS)
    },
    {
        'rhomb': [450, 250],
        'trajectory': [[450, 250], [450, 400]],
        'nosh': [450, 400],
        'rhomb_id': create_rhomb(can, 450, 250, RADUIS)
    },
    {
        'rhomb': [550, 250],
        'trajectory': [[550, 250], [550, 400]],
        'nosh': [550, 400],
        'rhomb_id': create_rhomb(can, 550, 250, RADUIS)
    },
    {
        'rhomb': [650, 250],
        'trajectory': [[650, 250], [650, 400]],
        'nosh': [650, 400],
        'rhomb_id': create_rhomb(can, 650, 250, RADUIS)
    },
    {
        'rhomb': [750, 250],
        'trajectory': [[750, 250], [750, 400]],
        'nosh': [750, 400],
        'rhomb_id': create_rhomb(can, 750, 250, RADUIS)
    },
    {
        'rhomb': [850, 250],
        'trajectory': [[850, 250], [850, 400]],
        'nosh': [850, 400],
        'rhomb_id': create_rhomb(can, 850, 250, RADUIS)
    },
]


drawlevel(can, level1)

# can.tag_bind(setsLists[0].get('rhomb_id'), BUTTON1, move_rhomb)
# can.tag_bind(setsLists[1].get('rhomb_id'), BUTTON1, move_rhomb)
# can.tag_bind(setsLists[2].get('rhomb_id'), BUTTON1, move_rhomb)

can.tag_bind(level1[0].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(level1[1].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(level1[2].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(level1[3].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(level1[4].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(level1[5].get('rhomb_id'), BUTTON1, move_rhomb)

fen.mainloop()