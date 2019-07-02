
from tkinter import *

root= Tk()

def printSample():
    print("Hello this is Tkinter World")
# command take function name and print on
# console and called as binding fn to widget
button=Button(root,text="This is interactable button"
              ,command=printSample)
button.pack()

def eventSample(event):
    print("Hello this is Tkinter World on Double Click")

button=Button(root,text="This is interactable button")
# bind will provide the event and fn bind with that event. Button-1 perform
# left click and Double-1 perform double click
button.bind("<Double-1>",eventSample)
button.pack()

root.mainloop()
