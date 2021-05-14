import tkinter, elements, random, consts

def number_pawn(listeGene):
    return len(listeGene)+1


def pawn_position():
    positionPion=[]
    positionPion.append(10*random.randint(20, 80))
    positionPion.append(10*random.randint(20, 60))
    return positionPion

def number_break():
    return random.randint(0,4)

def one_break(pI, pF):
    choix = [1, 2]
    L=[]
    c=random.choice(choix)
    if c==1: 
        L=[pI[0], pF[1]]
    else:
        L=[pF[0], pI[1]]
    return L
    
def two_break(pI, pF):
    choix = [1, 2]
    L=[]
    c=random.choice(choix)
    if c==1:
        L.append(10*random.randint(20, 80))
        L.append(pF[1])
    else:
        L.append(pF[0])
        L.append(10*random.randint(20, 60))
    L1=one_break(pI, L)
    trajectory=[L1,L]
    return trajectory

def three_break(pI, pF):
    choix = [1, 2]
    L=[]
    c=random.choice(choix)
    if c==1:
        L.append(10*random.randint(20, 80))
        L.append(pF[1])
    else:
        L.append(pF[0])
        L.append(10*random.randint(20, 60))
    L1=two_break(pI, L)
    trajectory=L1.append(L)
    return trajectory



def create_trajectory(pI, pF):
    nb_courbure=number_break()
    trajectory=[pI]
    if nb_courbure==1:
        trajectory+=one_break(pI, pF)
    elif nb_courbure==2:
        trajectory+=two_break(pI, pF)
    elif nb_courbure==3:
        trajectory+=three_break(pI, pF)
    trajectory.append(pF)
    return trajectory

def generator(setsLists):
    nombrePion=number_pawn(setsLists)
    listPart=[]
    for i in range(nombrePion):
        positionPion=pawn_position()
        positionEncoche=pawn_position()
        trajectoire=create_trajectory(positionPion, positionEncoche)
        eleDico= elements.elementsDictionnary(positionPion, trajectoire, positionEncoche, elements.create_rhomb(consts.can, positionPion[0], positionPion[1], consts.RADUIS))
        listPart.append(eleDico)
    return listPart
