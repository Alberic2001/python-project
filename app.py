import consts, elements, movement, solve


setsLists = [
    elements.elementsDictionnary([400, 100], [[400, 100], [400, 400], [700, 400], [700, 500]], [700, 500], 0),
    elements.elementsDictionnary([600, 100], [[600, 100], [600, 380]], [600, 380], 0),
    elements.elementsDictionnary([750, 700], [[750, 700], [750, 200]], [750, 200], 0),
    elements.elementsDictionnary([50, 760], [[50, 760], [750, 760]], [750, 760], 0)
]

elements.drawlevel(setsLists)

#solutions = solve.all_solutions(setsLists)
#print("Solver solutions = ", solutions)

#print(solve.solution(setsLists))

consts.can.tag_bind(setsLists[0].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))
consts.can.tag_bind(setsLists[1].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))
consts.can.tag_bind(setsLists[2].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))
consts.can.tag_bind(setsLists[3].get('rhomb_id'), consts.BUTTON1, lambda event, arg=setsLists: movement.move_rhomb(event, arg))


consts.fen.mainloop()