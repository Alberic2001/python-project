#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: alberic
"""

from tkinter import *
from math import *


def move_rhomb(event):
    global setsLists
    #print('setsLists: ', setsLists)
    for sets in setsLists:
        print('tag: ', sets.get('rhomb_id'), 'clicked tag: ', event.widget.find_withtag("current"))
        if sets.get('rhomb_id') == event.widget.find_withtag("current")[0]:
            move(sets)
            break





def move(sets):
    global dx, dy
    print(sets)
    trajectory = getTrajectory(sets)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcour les trajectoires possible
        #print('Boucle ', i, trajectory[i], trajectory[i+1])
        dx,dy=0,0
        x, y = trajectory[i][0], trajectory[i][1]
        mouvement(trajectory[i], trajectory[i+1], x, y)
        print(trajectory)
        

def mouvement(a, b, x, y):
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
        fen.after(10, mouvement(a, b, x, y))

