
from tkinter import *

root=Tk()

def onLeftclick(event):
    print("This is left click performed")

def onRightclick(event):
    print("This is right click performed")

def onMiddleClick(event):
    print("This is middle click performed")

# invisible frame with width and height
frame=Frame(root,width=300,height=250)
frame.bind("<Double-1>",onLeftclick)
frame.bind("<Button-3>",onRightclick)
# middle click is desktop mouse roller
frame.bind("<Button-1>",onMiddleClick)
frame.pack()
root.mainloop()
