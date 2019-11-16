from random import *
from tkinter import *
from time import *

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0

sleep(5)
while diapason < 1000:
    colors = choice(['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange',
                  'pink', 'purple', 'red','yellow', 'violet', 'indigo', 'chartreuse', 'lime'])
    x = randint(0, size)
    y = randint(0, size)
    d = randint(0, size/5)
    canvas.create_oval(x, y, x+d, y+d, fill=colors)
    root.update()
    diapason += 1
sleep(5)