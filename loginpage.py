from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("New Bihar Medical")
        self.root.geometry("1600x1200+0+0")

        #======All Images=============
        self.bg_icon= ImageTk.PhotoImage(Image.open("Images/bg2.jpg"))
        self.user_icon=ImageTk.PhotoImage(Image.open("Images/username.png"))
        self.pass_icon=ImageTk.PhotoImage(Image.open("Images/password.png"))
        self.logo_icon=ImageTk.PhotoImage(Image.open("Images/logo_nbm.png"))

        #==================Veriables===============
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_label = Label(self.root, image=self.bg_icon).pack()


        title=Label(self.root,text="Login System",font=("Copperplate Gothic Bold",40,"bold"),bg="royal blue",fg="Sky Blue",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="White")
        Login_Frame.place(x=550,y=150)

        logolabel=Label(Login_Frame,image=self.logo_icon,bd=0).grid(row=0,columnspan=2,pady=10)

        lableuser= Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("Courier New",15,"underline"),bg="White").grid(row=1,column=0,padx=5,pady=5)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("time new roman",15)).grid(row=1,column=1,padx=20)

        lablepassword= Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT,font=("Courier New", 15, "underline"),bg="White").grid(row=2, column=0, padx=5, pady=5)
        txtpass= Entry(Login_Frame, bd=5, relief=GROOVE,textvariable=self.pass_, font=("time new roman", 15)).grid(row=2, column=1, padx=20)

        btn_login=Button(Login_Frame,text="Login",width=10,font=("Arial",14,"bold"),bg="Blue",fg="White", command=self.login).grid(row=3,column=1,pady=10)


    def login(self):
        if self.uname.get()=="newbiharmedical" and self.pass_.get()=="nbm786":
            messagebox.showinfo("Sucessfull", f"Welcome{self.uname.get()}")
            self.root.destroy()
            import main
        elif self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error","All Fields are required!!!")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")







root= Tk()
obj=Login_System(root)
root.mainloop()