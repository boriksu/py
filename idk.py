from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('1000x1000')
canvas = Canvas(root,width=999,height=999)
canvas.pack()
pilImage = Image.open("ant.png")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
root.mainloop()