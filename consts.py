import tkinter, generatornum

RADUIS = 30  # Rayon du losange
dx, dy = 0, 0
BUTTON1 = '<Button-1>'

fen = tkinter.Tk()
fen.title("RHOMB")
can = tkinter.Canvas(fen, width=1000, height=800, bg="yellow")
can.pack()