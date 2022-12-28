import math
from tkinter import *
size = 600
radius1 = size / 2.9
#radius orbiti
radius2 = size / 100
#radius vrashaushegosya kruga
def coords(angle):
    x = math.cos(angle) * radius1
    y = math.sin(angle) * radius1
    return x - radius2 + size / 2, y - radius2 + size / 2, x + radius2 + size / 2, y + radius2 + size / 2

def motion(angle):
    angle = angle + speed
    c.coords(ball, coords(angle))
    root.after(int(abs(speed * 1000)), lambda: motion(angle))

angle = 0
speed = 0.1

root = Tk()
root.geometry('600x600')
root.configure(background = "grey")
c = Canvas(root, width=size, height=size)
c.pack()

c.create_oval(100, 100, 500, 500, width = 3)

ball = c.create_oval(250,50,350,150,fill = 'black')

motion(angle)

root.mainloop()




