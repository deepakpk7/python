import sqlite3
import tkinter


win=tkinter.Tk()
win.title("LOGIN")
win.minsize(500,500)
win.maxsize(800,800)
win.configure(bg="black")

def register():
    win1=tkinter.Tk()
    win1.title("REGISTER")
    win1.minsize(500,500)
    win1.maxsize(800,800)
    def reg():
        con=sqlite3.connect("python/Tkinter/user.db")
        # con.execute("create table user (uname text,password text)")
        con.execute("insert into user(uname,password)values(?,?)",(en1.get(),en3.get()))
        con.commit()
        win1.destroy()
    win1.configure(bg="black")
    l1=tkinter.Label(win1,text="Register Page",bg="green",fg="black")
    l1.pack()
    l2=tkinter.Label(win1,text="Name ",bg="green",fg="black")
    l2.place(x=80,y=40)
    en1=tkinter.Entry(win1)
    en1.place(x=200,y=40)
    # l3=tkinter.Label(win1,text="Email",bg="green",fg="black")
    # l3.place(x=80,y=70)
    # en2=tkinter.Entry(win1)
    # en2.place(x=200,y=70)
    l4=tkinter.Label(win1,text="password",bg="green",fg="black")
    l4.place(x=80,y=100)
    en3=tkinter.Entry(win1)
    en3.place(x=200,y=100)
    b1=tkinter.Button(win1,text="Register",bg="white",activebackground="white",fg="black",activeforeground="red",command=reg)
    b1.place(x=150,y=150)
    win1.mainloop()

# print username and password   
# def login():
#     print('username: ',e1.get())
#     l2. config(text=e1.get())
#     print('Password :',e2.get())
#     l3.config(text=e2.get())

def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text="Home Page")
    l1.pack()
    win2.minsize(500,500)
    win2.maxsize(800,800)
    win2.configure(bg="black")
    b1=tkinter.Button(win2,text="Logout",command=win2.quit)
    b1.pack()
    win2.mainloop()

def login():
    con=sqlite3.connect("python/Tkinter/user.db")
    data=con.execute("select * from user where uname=? and password=?",(e1.get(),e2.get()))
    f=0
    for i in data:
        f=1
        Home()
    if f==0:
        l4.config(text="INVALID USERNAME OR PASSWORD")
    

l1=tkinter.Label(win,text="Login Page",bg="green",fg="black")
l1.pack()
l2=tkinter.Label(win,text="username ",bg="green",fg="black")
l2.place(x=80,y=40)
e1=tkinter.Entry(win)
e1.place(x=200,y=40)
l3=tkinter.Label(win,text="password",bg="green",fg="black")
l3.place(x=80,y=70)
e2=tkinter.Entry(win)
e2.place(x=200,y=70)

b1=tkinter.Button(win,text="Register",bg="white",activebackground="white",fg="black",activeforeground="red",command=register)
b1.place(x=150,y=100)
b2=tkinter.Button(win,text="Login",bg="white",activebackground="white",fg="black",activeforeground="red",command=login)
b2.place(x=250,y=100)

l4=tkinter.Label(win)
l4.place(x=200,y=200)
win.mainloop()
