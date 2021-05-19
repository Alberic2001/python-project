from tkinter.constants import ALL
import elements, generatornum, consts, movement

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
    while True:
        print("aaaaaaaaaaaaaaa")
        for sets in level:
            a = sets.get('rhomb')
            b = sets.get('nosh')
            print(a, " ",b)
            if sets.get('rhomb') == sets.get('nosh'):
                print("bbbbbbbbbbbbbb = ",a)
                isCompleted = True
                return isCompleted

def switch(levelsList):
    consts.can.delete(ALL)
    levelsList.append(generatornum.generator(consts.i + 1))
    consts.i = consts.i + 1
    elements.drawlevel(levelsList[consts.i-1])
    tags = getAllRhombTags(levelsList[consts.i-1])
    for t in tags:
        consts.can.tag_bind(t, consts.BUTTON1, lambda event, arg=levelsList[consts.i-1]: movement.move_rhomb(event, arg))


def getAllRhombTags(level):
    tags = []
    for sets in level:
        tags.append(sets.get("rhomb_id"))
    return tags