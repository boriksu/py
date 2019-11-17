import fileinput
from random import *
from tkinter import *
from time import *

def draw_rooms(rooms):
    colors = choice(['pink', 'lime'])
    for key in rooms:
        x = rooms[key][0]
        y = rooms[key][1]
        canvas.create_oval(x, y, x+20, y+20, fill=colors)
        canvas.create_text(x + 10, y + 10, anchor=W, font="Purisa", text=key)


def draw_links(rooms, links):
    for el in links:
        f = rooms[el[0]]
        s = rooms[el[1]]
        canvas.create_line(f[0] + 10, f[1] + 10, s[0] + 10, s[1] + 10)

def read_map(rooms, links, action):
    for line in fileinput.input():
        line = line.rstrip()
        print(line)
        if line != "" and line[0] == 'L':
            action.append(line)
        elif line.find(' ') != -1:
            new = line.split(maxsplit=1)
            coordi = new[1].split(' ')
            coordi[0] = (int(coordi[0])  + 10) * 15
            coordi[1] = (int(coordi[1])  + 10) * 15
            rooms[new[0]] = coordi
        elif line.find('-') != -1:
            new = line.split('-')
            links.append(new)

rooms = {}
links = []
action = []
size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
read_map(rooms, links, action)
draw_rooms(rooms)
draw_links(rooms, links)
print(action)

canvas.create_rectangle(230, 10, 290, 60, outline='black', fill='black', width=1)

root.update()
#sleep(10)
#input('Press ENTER to exit')
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()