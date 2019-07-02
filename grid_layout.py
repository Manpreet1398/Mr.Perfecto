
from tkinter import *

root=Tk()

name=Label(root,text="Email")
password=Label(root,text="Password")

entry1=Entry(root)
entry2=Entry(root)
# by default column =0 and grid helps in putting label
# on window and sticky takes values as North/South/West/East
name.grid(row=0,column=0,sticky=E)
password.grid(row=1,sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

checkbox=Checkbutton(root,text="Keep me logged in")
# columnspan will merge 2 cells in one cell and place widget in middle
checkbox.grid(columnspan=2)
root.mainloop()
