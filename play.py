import tkinter, consts, elements, generatornum

def switchLevel(levelsList, i):
    levelsList.append(generatornum.generator(i))
    elements.drawlevel(levelsList[i])
    if levelCompleted(levelsList[i]) == True:
        switchLevel(levelsList, i+1)


def levelCompleted(level):
    isCompleted = False
    for sets in level:
        if sets.get('rhomb') == sets.get('nosh'):
            isCompleted = True
    return isCompleted

