import tkinter, consts

def getTrajectory(sets):
    return sets.get("trajectory")

def getRhombTag(sets):
    return sets.get("rhomb_id")


def overlaps(firstSet, secondSet):
    "Determine si deux pions (losanges) se chevauchent ou pas"
    overlaping = False
    i, j = firstSet.get('rhomb'), secondSet.get('rhomb')
    x, y, xprim, yprim = i[0], i[1], j[0], j[1]
    if abs(yprim - y) <= consts.RADUIS*2 and abs(xprim - x) <= consts.RADUIS * 2:
        print(yprim - y, xprim - x, consts.RADUIS)
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


def move_rhomb(event, setsLists):
    for sets in setsLists:
        if sets.get('rhomb_id') == event.widget.find_withtag("current")[0]:
            move(sets, setsLists)
            break

def move(sets, setsLists):
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
        print(mouvement(trajectory[i], trajectory[i+1], x, y, dic, setsLists))
        

def mouvement(a, b, x, y, sets, setsLists):
    global dx, dy
    #print("point, x, y = ", b, x,y)
    dx, dy = direction(a, b, x, y)

    x = x+(dx*10)
    y = y+(dy*10)
    sets.update({'rhomb': [x, y]})
    #print(sets.get('rhomb'))
    consts.can.coords(sets.get('rhomb_id'),
            x-consts.RADUIS, y,
            x, y-consts.RADUIS,
            x+consts.RADUIS, y,
            x, y+consts.RADUIS
            )
        #print(2)
    if global_overlaps(sets, setsLists) != True:    
        if x != b[0] or y != b[1]:
            #print(1)
            consts.fen.after(30, mouvement, a, b, x, y, sets, setsLists)
    else: 
        return False


def direction(a, b, x, y):
    dx, dy = 0, 0
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
    return dx, dy
