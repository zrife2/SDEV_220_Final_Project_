from tkinter import  *
from tkinter import messagebox

def login():
    username=Entry1.get()
    password=Entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","blank not allowed")

    elif (username=="john" and password=="123"):
            messagebox.showinfo("","logged in")

    else:
            messagebox.showinfo("","incorrect username and password")

root=Tk()
root.title("login")
root.geometry("300x300")

global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=70)

Entry1=Entry(root,bd=5)
Entry1.place(x=140,y=20)

Entry2=Entry(root,bd=5)
Entry2.place(x=140,y=70)

Button(root,text="Login", command=login,height=3,width=13,bd=6).place(x=100,y=120)

root.mainloop()

