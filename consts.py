import tkinter, generatornum

RADUIS = 30  # Rayon du losange
dx, dy = 0, 0
BUTTON1 = '<Button-1>'
i = 1

fen = tkinter.Tk()
fen.title("RHOMB")
can = tkinter.Canvas(fen, width=1000, height=800, bg="yellow")
arrowright = can.create_polygon(950,20,980,40,950,60,fill="#4389fe")
can.pack()

# setsLists = generatornum.generator(1)

levelsLists = []
# levelsLists.append(setsLists)

