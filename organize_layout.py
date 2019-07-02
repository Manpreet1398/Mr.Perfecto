
from tkinter import *

root=Tk()

# create invisible frame at the top
topFrame=Frame(root)
# by default it goes to top as we have bottom frame
topFrame.pack()
bottomFrame=Frame(root)
# In order to place invisible frame to bottom
bottomFrame.pack(side=BOTTOM)
# creating buttons
button1=Button(topFrame,text="Button1",fg="red")
button2=Button(topFrame,text="Button2",fg="green")
button3=Button(topFrame,text="Button3",fg="purple")
button4=Button(bottomFrame,text="Button4",fg="blue")

# in order to dislpay widget
# as we are using pack , it will be packed as per frame
# assigned
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)




root.mainloop()
