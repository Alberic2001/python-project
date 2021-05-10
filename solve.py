from tkinter import *
import sys
import test


# Le solveur de rhomb
# Nous utiliserons la methode backtracking
# Comment cela se passe t-il ?
# un level du jeu est represente par une liste de dictionnaires
# Les dictionnaires contiennent nos ensembles pion-trajectoire-encoche-tagDuPion
# un pion est represente par un liste de ses coordonnees, idem pour les encoches
# la trajectoire est representee par une liste de liste de toutes les coordonnees des
# points ou un pion change de trajectoire lors d un mouvement
# Avec cette grande liste de dictionnaires, on recupere les tags de nos pions et on les 
# regroupe dans une liste propre T par exemple
# On cree une nouvelle liste S qui sera notre liste de solution contenant les tags dans
# l ordre de clic
# Pour chaque element de la liste T on verifie si a un moment du delacement du pion elle
# heurte un autre pion de la liste avec la methode overlaps deja definie
# Si ce n'est pas le cas on ajoute ce tag dans la liste des solutions S
# Si c'est le cas on arrete le parcours et on passe a un autre pion de la liste T
# Et on reprend le meme procede de maniere recursive

# T = liste de tous les tags des pions du level
# level = liste de tous les dictionnaires du level
# N = liste des pions qui en chevauchent d'autres

def all_solutions(level):
    solutions = []
    for i in range(len(level)-1):
        solutions.append(solver(level))
    return solutions

def solver(level):
    S, N = [], []
    solution = resolve(level, S, N)
    if len(solution) == len(level):
        return solution
    else:
        return False


def resolve(level, S, N):
    print("resolve test")
    for i in range(len(level)-1):
        if test.move(level[i]) == None:
            S.append(level[i])
        else:
            N.append(level[i])

    if N != []:
        NN = N
        S = N
        resolve(N, S, NN)
    else:
        return S


solutions = all_solutions(test.setsLists)
print(solutions)

# erreur => provient du fait que le solver est appele avant la creation des pions




# solver definie de maniere recursive (pas totalement )        
# def solver(level, tag):
#     # Initialisation de la liste de la solution
#     S = []
#     resolve(level, tag, S)
    

# def resolve(level, tag, S):
#     isSolvable = True
#     print(S)
#     if tag < len(level):
#         dic = level[tag]
#         if dic not in S:
#             if test.move(dic) == None:
#                 S.append(dic)
#                 # print("Appel recursif")
#                 resolve(level, tag+1, S)
#             else:
#                 resolve(level, tag+1, S)
#     return isSolvable

















# for i in range(len(T)-1)
# if level[i-1] not in S:
#             if test.move(level[i-1]) == None:
#                 S.append(level[i-1])
#             else:
#                 if tag < len(T):
#                     isSolvable = solve(T, level, tag+1) and isSolvable