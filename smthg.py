from tkinter import *
from time import *

def animate():
    global i
    c.move(ball, 6, 0)
    i = i + 1
    c.update()
    sleep(1)
    print('hello', i)
    #root.after(45, animate)

root = Tk()
i = 0
c = Canvas(root, width = 200, height = 100)
c.pack()
ball = c.create_oval(0, 25, 50, 75)
for i in range(10):
    animate()
root.mainloop()