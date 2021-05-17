import tkinter, elements, random, consts

def number_pawn(listeGene):
    return len(listeGene)+1


def pawn_position():
    positionPion=[]
    positionPion.append(10*random.randint(10, 90))
    positionPion.append(10*random.randint(10, 70))
    return positionPion

def number_break(pI, pF):
    if pI[0]==pF[0] or pI[1]==pF[1]:
        return random.randint(0,3)
    else:
        return random.randint(1,3)

def one_break(pI, pF):
    choix = [1, 2]
    c=random.choice(choix)
    if c==1: 
        L=[pF[0], pI[1]]
    else:
        L=[pI[0], pF[1]]
    return [L]
    
def two_break(pI, pF):
    choix = [1, 2]
    L=[]
    c=random.choice(choix)
    if c==1:
        L.append(10*random.randint(10, 90))
        L.append(pI[1])
        L1=[L[0], pF[1]]
    else:
        L.append(pI[0])
        L.append(10*random.randint(10, 70))
        L1=[pF[0], L[1]]
    
    #L1=one_break(L, pF)
    trajectory=[L,L1]
    return trajectory

def three_break(pI, pF):
    choix = [1, 2]
    L=[]
    L1=[]
    c=random.choice(choix)
    if c==1:
        L.append(10*random.randint(10, 90))
        L.append(pI[1])

        L1=[L[0]]
        L1.append(10*random.randint(10, 70))

        L2=[pF[0],L1[1]]
    else:
        L.append(pI[0])
        L.append(10*random.randint(10, 70))

        L1.append(10*random.randint(10, 90))
        L1.append(L[1])

        L2=[L1[0],pF[1]]

    trajectory=[L,L1,L2]
    return trajectory



def create_trajectory(pI, pF):
    nb_courbure=number_break(pI, pF)
    print(nb_courbure)
    trajectory=[pI]
    if nb_courbure==1:
        trajectory+=one_break(pI, pF)
    elif nb_courbure==2:
        trajectory+=two_break(pI, pF)
    elif nb_courbure==3:
        trajectory+=three_break(pI, pF)
    trajectory.append(pF)
    return trajectory

def generator(a):
    listPart=[]
    for i in range(a):
        positionPion=pawn_position()
        positionEncoche=pawn_position()
        trajectoire=create_trajectory(positionPion, positionEncoche)
        print (positionPion,positionEncoche,trajectoire)
        eleDico= elements.elementsDictionnary(positionPion, trajectoire, positionEncoche, elements.create_rhomb(consts.can, positionPion[0], positionPion[1], consts.RADUIS))
        listPart.append(eleDico)
    return listPart
