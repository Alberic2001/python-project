import tkinter, consts
from tkinter.constants import ALL

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

def drawlevel(level):
    consts.can.delete(ALL)
    for sets in level:
        sets.update({'rhomb_id': create_rhomb(consts.can, sets.get('rhomb')[0], sets.get('rhomb')[1])})
    for sets in level:
        create_trajectory(consts.can, sets.get('trajectory'))
        create_nosh(consts.can, sets.get('nosh')[0], sets.get('nosh')[1])