import tkinter

win=tkinter.Tk()
win.title("APPLICATION")
win.minsize(500,500)
win.maxsize(800,800)
win.configure(bg="black")

def save():
    l2.config(text=e1.get())
# LABEL 
l=tkinter.Label(win,text="Welcome All",bg="green")
l.pack()

# ADD TEXT BOX
e1=tkinter.Entry(win)
e1.pack()

# ADD BUTTON
b1=tkinter.Button(win,text="View",bg="white",activebackground="white",fg="black",activeforeground="red",command=save)
b2=tkinter.Button(win,text="Save",bg="white",activebackground="white",fg="black",activeforeground="red")
b1.pack(),b2.pack()

l2=tkinter.Label(win)
l2.pack()

win.mainloop()