import fileinput
from random import *
from tkinter import *
from time import *

def draw_rooms(rooms):
    colors = choice(['lime', 'lime'])
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
    global num
    num = input()
    for line in fileinput.input():
        line = line.rstrip()
        print(line)
        if line != "" and line[0] == 'L':
            action.append(line)
        elif line.find(' ') != -1:
            new = line.split(maxsplit=1)
            coordi = new[1].split(' ')
            coordi[0] = (int(coordi[0])  + 10) * 20
            coordi[1] = (int(coordi[1])  + 10) * 20
            rooms[new[0]] = coordi
        elif line.find('-') != -1:
            new = line.split('-')
            links.append(new)

def draw_ant(key):
    global rooms
    x = rooms[key][0]
    y = rooms[key][1]
    ant = canvas.create_rectangle(x + 3, y + 3, x+14, y + 14, outline='black', fill='black', width=1, tag='ant')


def draw_action(action):
    global num
    f = 0
    newa = "L" + num
    draw_ant('start')
    root.update()
    sleep(2)
    for value in action:
        canvas.delete('ant')
        if (f == 0):
            if (value.find(newa) != -1):
                f = 1
            else:
                draw_ant('start')
        new = value.split(' ')
        for value1 in new:
            new1 = value1.split('-')
            draw_ant(new1[1])
        root.update()
        sleep(1)



rooms = {}
links = []
action = []
num = ""
size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
read_map(rooms, links, action)
draw_rooms(rooms)
draw_links(rooms, links)
print(action)

#допустим, я знаю start и end уже
#движение одного муравья


root.update()
draw_action(action)

#sleep(10)
#input('Press ENTER to exit')
Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()