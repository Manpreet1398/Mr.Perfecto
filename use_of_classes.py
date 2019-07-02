
from tkinter import *
import sys
class EventsHandling:
    # master means main window
    def __init__(self,master):
        self.master=master
        frame=Frame(self.master)
        frame.pack()
        self.printButton=Button(frame,text="this will print",command=self.printMessage)
        self.printButton.pack(side=LEFT)
        # frame.quit will quit main loop and closing and
        # ending the program
        self.quitButton = Button(frame, text="this will quit session", command=frame.quit)
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print("this will print in console")


root=Tk()

event=EventsHandling(root)


root.mainloop()
