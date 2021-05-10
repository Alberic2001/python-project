#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:49:46 2021
@author: alberic
"""

import tkinter
import sys
import time
# --------------------------Fonctions de creation d'elements graphiques--------------------------

# Creer un rhomb

def hello():
    print("hello")


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

def create_curve(canvas, trajectory_coordinates):
    coul = "#1875d1"
    for i in range(len(trajectory_coordinates)-2):
        canvas.create_line(
            trajectory_coordinates[i][0],
            trajectory_coordinates[i][1],
            trajectory_coordinates[i+1][0],
            trajectory_coordinates[i+1][1],
            trajectory_coordinates[i+2][0],
            trajectory_coordinates[i+2][1],
            fill=coul,
            width=3,
            smooth=1
        )
    return trajectory_coordinates

def create_nosh(canvas, x, y, raduis=30):
    nosh = canvas.create_polygon(x-raduis, y,
                                 x, y-raduis,
                                 x+raduis, y,
                                 x, y+raduis,
                                 fill='', outline='#4389fe', width=3)
    return nosh

def drawCurvedLine(canvas,x1,y1,x2,y2,x3,y3):
    return canvas.create_line(x1,y1,x2,y2,x3,y3,fill="#1875d1",width=3,smooth=1)



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
    overlaping = False
    i, j = firstSet.get('rhomb'), secondSet.get('rhomb')
    x, y, xprim, yprim = i[0], i[1], j[0], j[1]
    if abs(yprim - y) <= RADUIS*2 and abs(xprim - x) <= RADUIS * 2:
        print(yprim - y, xprim - x, RADUIS)
        overlaping = True
    return overlaping

def global_overlaps(sets, level):
    "Determine si un pion chevauche le reste des pions ou pas"
    isOverlaping = False
    for i in range(len(level)-1):
        if level[i] != sets:
            isOverlaping = overlaps(sets, level[i])
            if isOverlaping == True:
                break
    return isOverlaping


def move_rhomb(event):
    global setsLists
    for sets in setsLists:
        if sets.get('rhomb_id') == event.widget.find_withtag("current")[0]:
            move(sets)
            break

def move(sets):
    global dx, dy
    dic = sets
    #print(sets)
    trajectory = getTrajectory(dic)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcourt les trajectoires possible
        dx,dy=0,0
        #print("Boucle ",i)
        x, y = trajectory[i]
        #print(x,y)
        print(dic.get('rhomb'))
        print(mouvement(trajectory[i], trajectory[i+1], x, y, dic))
        

def mouvement(a, b, x, y, sets):
    global dx, dy, setsLists
    #print("point, x, y = ", b, x,y)
    if a[0] / b[0] == 1:
        # Mvt suivant l'axe des ordonnees, vertical
        if y <= b[1]:
            dx,dy = 0,1
        else:
            dx,dy = 0,-1

    if a[1] / b[1] == 1:
        # Mvt suivant l'axe des abcisses, horizontal
        if x <= b[0]:
            dx,dy = 1,0
        else:
            dx,dy = -1,0
    if a[0] / b[0] != 1 and a[1] / b[1] != 1:
        if y <= b[1]:
            dx,dy = 0,1
        else:
            dx,dy = 0,-1

    
    
    x = x+(dx*10)
    y = y+(dy*10)
    sets.update({'rhomb': [x, y]})
    #print(sets.get('rhomb'))
    can.coords(sets.get('rhomb_id'),
            x-RADUIS, y,
            x, y-RADUIS,
            x+RADUIS, y,
            x, y+RADUIS
            )
        #print(2)
    if global_overlaps(sets, setsLists) != True:    
        if x != b[0] or y != b[1]:
            #print(1)
            fen.after(30, mouvement, a, b, x, y, sets)
    else: 
        return False
        

# --------------------------Consts--------------------------
RADUIS = 30  # Rayon du losange
dx, dy = 0, 0
BUTTON1 = '<Button-1>'

fen = tkinter.Tk()
fen.title("RHOMB")
can = tkinter.Canvas(fen, width=1000, height=800, bg="yellow")
can.pack()


#TEST
'''print(overlaps(
        elementsDictionnary([15,15], [[30,30], [500,30], [500,400], [300,400]], [330, 400], create_rhomb(can, 15,15, RADUIS)),
        elementsDictionnary([400,15], [[400,45], [700,45], [700,145]], [700, 175], create_rhomb(can, 400,15, RADUIS))
    ))
'''
setsLists = [
    elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [700, 500]], [700, 500], create_rhomb(can, 400, 100, RADUIS)),
    elementsDictionnary([600, 100], [[600, 100], [600, 380]], [600, 380], create_rhomb(can, 600, 100, RADUIS)),
    elementsDictionnary([750, 700], [[750, 700], [750, 200]], [750, 300], create_rhomb(can, 750, 700, RADUIS)),
]
for sets in setsLists:
    create_trajectory(can, sets.get('trajectory'))
    create_nosh(can, sets.get('nosh')[0], sets.get('nosh')[1])


can.tag_bind(setsLists[0].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(setsLists[1].get('rhomb_id'), BUTTON1, move_rhomb)
can.tag_bind(setsLists[2].get('rhomb_id'), BUTTON1, move_rhomb)



fen.mainloop()