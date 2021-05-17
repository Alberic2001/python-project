import elements, generatornum

def switchLevel(levelsList, i):
    print('switched')
    levelsList.append(generatornum.generator(i))
    elements.drawlevel(levelsList[i-1])
    # if levelCompleted(levelsList[i-1]) == True:
    #     print('completed')
    #     consts.fen.after(30, switchLevel, levelsList, i+1)
    # consts.fen.after(10000, switchLevel, levelsList, i)

def levelCompleted(level):
    isCompleted = False
    for sets in level:
        if sets.get('rhomb') == sets.get('nosh'):
            isCompleted = True
    return isCompleted

