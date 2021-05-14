import generator
import consts, elements, movement, solve

 

setsLists = [
    elements.elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [700, 500]], [700, 500], elements.create_rhomb(consts.can, 400, 100, consts.RADUIS)),
    elements.elementsDictionnary([600, 100], [[600, 100], [600, 380]], [600, 380], elements.create_rhomb(consts.can, 600, 100, consts.RADUIS)),
    elements.elementsDictionnary([750, 700], [[750, 700], [750, 200]], [750, 200], elements.create_rhomb(consts.can, 750, 700, consts.RADUIS)),
]
# setsLists = generator.generator([])
# print(setsLists)
for sets in setsLists:
    elements.create_trajectory(consts.can, sets.get('trajectory'))
    elements.create_nosh(consts.can, sets.get('nosh')[0], sets.get('nosh')[1])

print(solve.solution(setsLists))

#consts.can.tag_bind(setsLists[index].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))


consts.can.tag_bind(setsLists[0].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))
# consts.can.tag_bind(setsLists[1].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))
# consts.can.tag_bind(setsLists[2].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))


consts.fen.mainloop()