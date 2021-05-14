import tkinter, movement, vect

def move_solver(sets, setsLists):
    global dx, dy
    #dic = sets
    #print(sets)
    trajectory = movement.getTrajectory(sets)  # ====liste des trajectoires
    for i in range(len(trajectory)-1):  # on parcourt les trajectoires possible
        dx,dy=0,0
        #print("Boucle ",i)
        x, y = trajectory[i]
        #print(x,y)
        return mouvement_solver(trajectory[i], trajectory[i+1], x, y, sets, setsLists)
        #mouvement_solver(trajectory[i], trajectory[i+1], x, y, sets, setsLists)


def mouvement_solver(a, b, x, y, sets, setsLists):
    global dx, dy
    #print("point, x, y = ", b, x,y)
    dx, dy = movement.direction(a, b, x, y)
    x = x+(dx*10)
    y = y+(dy*10)
    #sets.update({'rhomb': [x, y]})    
    if movement.global_overlaps(sets, setsLists) != True:    
        if x != b[0] or y != b[1]:
            #print(1)
            sets.update({'rhomb': [x, y]})
            mouvement_solver(a, b, x, y, sets, setsLists)
            return True
    else: 
        return False


#SOLVER
def all_solutions(level):
    solutions = []
    for i in range(len(level)-1):
        solutions.append(solver(level))
    return solutions

def solver(level):
    S, N = [], []
    solution = resolve(level, S, N)
    # if len(solution) == len(level):
    return solution
    # else:
    #     return False


def resolve(level, S, N):
    print("resolve test")
    for i in range(len(level)):
        if move_solver(level[i], level) != False:
            S.append(level[i])
        else:
            N.append(level[i])

    if N != []:
        NN = N
        S = N
        resolve(N, S, NN)
    else:
        return S



# Autre essai de solver
def getDic(tag, level):
    for i in level:
        if i.get('rhomb_id') == tag:
            return i

def getAllTags(level):
    T = []
    for i in level:
        T.append(i.get('rhomb_id'))
    return T

def turnIntoGraph(level):
    G = [[]]
    T = getAllTags(level)
    for i in level:
        G.append(T)
    print(G)
    return G


def resolve(G, i, Visite, ordreVisite, level):
    ordreVisite.append(i)
    print("Début du parcours du sommet ",i)
    print("Etat du vecteur de visite ",Visite)
    print("Ordre de visite", ordreVisite)
    
    Visite[i]=1
    for j in G[i]:
        if Visite[j]==0:
            #print("Appel récursif  ",j)
            if move_solver(level[i-1], level) == True:
                resolve(G,j,Visite,ordreVisite,level)
        else:
            print("Revisite du pion ",j)
    print("Fin du parcours de ", i)


def solver(G, level):
    #initialisation du vecteur de visite
    Visite=vect.initVect(len(G),0)  
    ordreVisite=[]
    for i in range(1,len(G)):
        print("bla bla ", G[i], i)
        #if Visite[i]==0:
        newOrdre=[]
        resolve(G,i,Visite,newOrdre,level)
        ordreVisite.append(newOrdre)
        print("Ordre de visite solver = ",ordreVisite)
        Visite=vect.initVect(len(G),0)
    return ordreVisite


def solution(level):
    # G = turnIntoGraph(level)
    # print("G = ",G )
    return solver([[], [2, 3], [1, 3], [1, 2]], level)

