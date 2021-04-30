#! / usr / bin / env python3
# - * - codage: utf-8 - * -
"" "
Créé le sam.10 avril 10:49:46 2021
@auteur: alberic
"" "

à partir de l'  importation tkinter  * 
à partir de l'  importation mathématique  * 

# -------------------------- Fonctions de création d'éléments graphiques ---------------- ----------

# Creer un rhomb


def  create_rhomb ( canevas , x , y , raduis = 30 ):
    r1  =  toile . create_polygon ( x - raduis , y ,
                               x , y - raduis ,
                               x + raduis , y ,
                               x , y + raduis ,
                               fill = "# 4389fe" )
    r2  =  toile . create_polygon ( x - ( raduis - 15 ), y ,
                               x , y - ( raduis - 15 ),
                               x + ( raduis - 15 ), y ,
                               x , y + ( raduis - 15 ),
                               fill = "# 1875d1" )
    retour [ r1 , r2 ]


def  create_stick ( canevas , débuts , fin ):
    retour de la  toile . create_line ( debut [ 0 ], debut [ 1 ], end [ 0 ], end [ 1 ], fill = "# 1875d1" , width = 3 )


def  create_trajectory ( canvas , trajectory_coordinates ):
    coul  =  "# 1875d1"
    pour  i  dans l'  intervalle ( len ( trajectory_coordinates ) - 1 ):
        toile . create_line ( trajectoire_coordonnées [ i ] [ 0 ],
                           trajectory_coordinates [ i ] [ 1 ],
                           trajectoire_coordonnées [ i + 1 ] [ 0 ],
                           trajectoire_coordonnées [ i + 1 ] [ 1 ],
                           fill = coul ,
                           largeur = 3
                           )


def  create_nosh ( canevas , x , y , raduis = 30 ):
    nosh  =  toile . create_polygon ( x - raduis , y ,
                                 x , y - raduis ,
                                 x + raduis , y ,
                                 x , y + raduis ,
                                 fill = '' , contour = '# 4389fe' , largeur = 3 )
    retourner  nosh


def  elementsDictionnary ( rhomb_coordinates , trajectory_coordinates , nosh_coordinates , rhombs_id_list ):
    "Permet la création du dictionnaire contenant tous les éléments d'un ensemble"
    # rhomb_coordinates represente les coordonnes du centre d'un losange
    # trajectory_coordinates represente la liste des points qui achètent la création de la trajectoire
    # nosh_coordinates represente les coordonnes du centre de l'encoche
    # rhomb_id_lists est la liste des deux id representant les losanges crees (create_rhomb)
    retour {
        'rhomb' : coordonnées_ rhomb ,
        'trajectoire' : trajectoire_coordonnées ,
        'nosh' : nosh_coordinates ,
        'rhomb_id' : rhombs_id_list
    }


def  getTrajectory ( ensembles ):
     ensembles de retour . get ( "trajectoire" )


'' '
def getAllTrajectories (setsLists):
    allTrajectories = []
    pour i dans les ensembles
        allTrajectories.append (getTrajectory (i))
    renvoyer toutTrajectoires
'' '


def  chevauche ( firstSet , secondSet ):
    "Déterminer si deux pions (losanges) se chevauchent ou pas"
    # firstSet et secondSet sont des ensembles
    chevauchement  =  Faux
    i , j  =  firstSet . get ( 'losange' ), secondSet . obtenir ( 'losange' )
    x , y , xprim , yprim  =  i [ 0 ], i [ 1 ], j [ 0 ], j [ 1 ]
    si  yprim  -  y  <=  RADUIS * 2  et  xprim  -  x  <=  RADUIS  *  2 :
        impression ( yprim  -  y , xprim  -  x , RADUIS )
        chevauchement  =  Vrai
    retour se  chevauchant


'' '
def move (ensembles):
    #sets = ensemble
    x, y = sets.get ('losange') [0], sets.get ('losange') [1]
    trajectoire = getTrajectory (ensembles)
    dx, dy = 0, 0
    pour i dans la plage (len (trajectoire) -1):
        #print (trajectoire [i: i + 2])
        si trajectoire [i] [0] / trajectoire [i + 1] [0] == 1:
            #Mvt suivant l'observation des ordonnées
            si y <= trajectoire [i + 1] [1]:
                y, dx, dy = y + (RADUIS * 2), dx, RADUIS
        si trajectoire [i] [1] / trajectoire [i + 1] [1] == 1:
            #Mvt suivant l'observation des abcisses
            si x <= trajectoire [i + 1] [0]:
                x, dx, dy = x + (RADUIS * 2), RADUIS, dy
        si trajectoire [i] [0] / trajectoire [i + 1] [0]! = 1 et trajectoire [i] [1] / trajectoire [i + 1] [1]! = 1:
            #Mvt oblique
            x, y, dx, dy = x + (RADUIS * 2), y + (RADUIS * 2), trajectoire [i] [0] / trajectoire [i + 1] [0], trajectoire [i] [1] / trajectoire [ i + 1] [1]
        sets.get ('rhomb') [0], sets.get ('rhomb') [1] = x, y
        
        can.coords (sets.get ('rhomb_id') [0], sets.get ('rhomb') [0], sets.get ('rhomb') [1], sets.get ('rhomb') [0 ] + RADUIS, sets.get ('losange') [1] + RADUIS)
        can.coords (sets.get ('rhomb_id') [1], sets.get ('rhomb') [0], sets.get ('rhomb') [1], sets.get ('rhomb') [0 ] + RADUIS, sets.get ('losange') [1] + RADUIS)
    fen.after (20, déplacer (ensembles))
def move_rhomb (événement):
    ensembles globaux
    pour les ensembles dans les ensembles
        déplacer (ensembles)
    
'' '
'' '
def déplacer ():
    ensembles globaux
    x, y = sets.get ('losange') [0], sets.get ('losange') [1]
    trajectoire = getTrajectory (ensembles)
    dx, dy = 0, 0
    i = 0
    si trajectoire [i] [0] / trajectoire [i + 1] [0] == 1:
        #Mvt suivant l'observation des ordonnées
        si y <= trajectoire [i + 1] [1]:
            y, dx, dy = y + (RADUIS * 2), dx, RADUIS
    si trajectoire [i] [1] / trajectoire [i + 1] [1] == 1:
        #Mvt suivant l'observation des abcisses
        si x <= trajectoire [i + 1] [0]:
            x, dx, dy = x + (RADUIS * 2), RADUIS, dy
    si trajectoire [i] [0] / trajectoire [i + 1] [0]! = 1 et trajectoire [i] [1] / trajectoire [i + 1] [1]! = 1:
        #Mvt oblique
        x, y, dx, dy = x + (RADUIS * 2), y + (RADUIS * 2), trajectoire [i] [0] / trajectoire [i + 1] [0], trajectoire [i] [1] / trajectoire [ i + 1] [1]
    sets.get ('rhomb') [0], sets.get ('rhomb') [1] = x, y
    can.coords (sets.get ('rhomb_id') [0], sets.get ('rhomb') [0], sets.get ('rhomb') [1], sets.get ('rhomb') [0 ] + RADUIS, sets.get ('losange') [1] + RADUIS)
    can.coords (sets.get ('rhomb_id') [1], sets.get ('rhomb') [0], sets.get ('rhomb') [1], sets.get ('rhomb') [0 ] + RADUIS, sets.get ('losange') [1] + RADUIS)
    i + = 1
    fen.après (20, déplacer)
'' '


def  move ( ensembles ):
    #sets = ensemble
    global  dx , dy
    x , y  =  ensembles . get ( 'rhomb' ) [ 0 ], définit . get ( 'losange' ) [
        1 ]   # === les coordonés x, y du losange
    trajectory  =  getTrajectory ( sets )   # ==== liste des trajectoires
    for  i  in  range ( len ( trajectory ) - 1 ):   # on parcour les trajectoires possible
        #print (trajectoire [i], trajectoire [i + 1])
        # Pause
        dx , dy = 0 , 0
        imprimer ( 'Boucle' , i )
        mouvement ( trajectoire [ i ], trajectoire [ i + 1 ], x , y )


def  mouvement ( a , b , x , y ):
    global  dx , dy
    # on vérifie si xi = xi + 1
    
    si  a [ 0 ] /  b [ 0 ] ==  1 :
        # Mvt suivant l'axe des ordonnées, vertical
        si  y  <=  b [ 1 ]:
            #y, dx, dy = y + (RADUIS * 2), dx, RADUIS
            dx  =  0
            dy  =  1
        sinon :
            dx  =  0
            dy  =  - 1

    si  a [ 1 ] /  b [ 1 ] ==  1 :
        # Mvt suivant l'observation des abcisses, horizontal
        si  x  <=  b [ 0 ]:
            #x, dx, dy = x + (RADUIS * 2), RADUIS, dy
            dx  =  1
            dy  =  0
        sinon :
            dx  =  - 1
            dy  =  0
    x  =  x + ( dx * 10 )
    y  =  y + ( dy * 10 )
    # affecter la ligne de trajectoire

    #x, y, dx, dy = x + (RADUIS * 2), y + (RADUIS * 2), trajectoire [i] [0] / trajectoire [i + 1] [0], trajectoire [i] [1] / trajectoire [i + 1] [1]
    # ne pas affecter le dictionnaire principal ???
    ensembles . get ( 'rhomb' ) [ 0 ], définit . get ( 'losange' ) [ 1 ] =  x , y
    peut . coords ( ensembles . get ( 'rhomb_id' ) [ 0 ],
               x - RADUIS , y ,
               x , y - RADUIS ,
               x + RADUIS , y ,
               x , y + RADUIS
               )
    # can.coords (sets.get ('rhomb_id') [0],
    # x- (RADUIS-15), y,
    # x, y- (RADUIS-15),
    # x + (RADUIS-15), y,
    # x, y + (RADUIS-15)
    #)   

    si  x  ! =  b [ 0 ] et  y  ! =  b [ 1 ]:
        #print (x, y, a, b)
        print ( 'Récursif' )
        fen . après ( 10 , mouvement ( a , b , x , y ))


def  move_rhomb ( événement ):
    ensembles  globaux
    déplacer ( setsLists [ 0 ])


# -------------------------- Consts ---------------------- ----
RADUIS  =  30   # Rayon du losange
dx , dy  =  0 , 0

fen  =  Tk ()
can  =  Toile ( fen , largeur = 1000 , hauteur = 800 , bg = "jaune" )
peut . tag_click  =  Vrai
peut . pack ( padx = 5 , pady = 5 )


# TEST
#allTrajectories = getAllTrajectories (setsLists)
#print (len (allTrajectories), allTrajectories)

'' 'impression (chevauche (
        elementsDictionnaire ([15,15], [[30,30], [500,30], [500,400], [300,400]], [330, 400], create_rhomb (can, 15,15, RADUIS)),
        elementsDictionnaire ([400,15], [[400,45], [700,45], [700,145]], [700, 175], create_rhomb (can, 400,15, RADUIS))
    ))
'' '
setsLists  = [
    elementsDictionnaire ([ 400 , 100 ], [[ 400 , 100 ], [ 400 , 400 ], [ 700 , 400 ], [
                        700 , 500 ]], [ 700 , 500 ], create_rhomb ( can , 400 , 100 , RADUIS ))
]
pour les  ensembles  à  setsLists :
    create_trajectory ( peut , définit . get ( 'trajectoire' ))
    create_nosh ( peut , définit . get ( 'nosh' ) [ 0 ], définit . get ( 'nosh' ) [ 1 ])
    peut . tag_bind ( définit . get ( 'rhomb_id' ) [ 0 ], '<Button-1>' , move_rhomb )
    # can.tag_bind (sets.get ('rhomb_id') [1], '<Button-1>', move_rhomb)


fen . boucle principale ()