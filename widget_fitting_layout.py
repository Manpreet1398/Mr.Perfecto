
from tkinter import *

root=Tk()

one=Label(root,text="One",bg="red",fg="white")
one.pack()
two=Label(root,text="Two",bg="green",fg="black")
# this will fill the complete widget as wide
# as parent window is
two.pack(fill=X)
#
three=Label(root,text="Three",bg="blue",fg="red")
# # this will fill the complete window at left as wide as
# # left part of window is
three.pack(side=LEFT,fill=Y)
root.mainloop()
