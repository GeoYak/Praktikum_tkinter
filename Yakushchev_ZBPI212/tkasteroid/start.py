from tkinter import Tk, Button, Frame

from ship import Ship
from game import Game
from asteroids import Asteroids

root = Tk()
root.geometry('900x900')
asteroids = Asteroids(root)
game = Game(root)
game.create_asteroids(asteroids)
game.update_asteroid()
def start():
    UI_frame.destroy()
    player = Ship(root)
    game.create_player(player)
    game.update_player()
    root.mainloop()

UI_frame = Frame(root, width=100, height=50)
UI_frame.place(relx=0.5, rely=0.5)
Button(UI_frame, text='Старт', command=start, bg='grey').pack()
root.mainloop()
