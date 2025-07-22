import tkinter
import random

width=1000
height =500

window= tkinter.Tk()
window.title("Snake Game")
window.resizable(False,False)

canvas=tkinter.Canvas(window,bg="black",width=width,height=height,borderwidth=0,highlightthickness=0)
canvas.pack()
window.mainloop()