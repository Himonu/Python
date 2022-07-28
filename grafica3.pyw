from tkinter import *

root = Tk()

mf = Frame(root, width=300, height=500)
mf.pack()

img = PhotoImage(file="alucard.gif")

Label(mf, image=img).place(x=100, y=200)


root.mainloop()