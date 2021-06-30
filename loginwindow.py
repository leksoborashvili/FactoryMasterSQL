from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk

class Login:

    def __init__(self, root, signIn):
        self.login = ttk.Frame(root)

        ttk.Label(self.login, text = "Username", font = "10", justify = "center").grid(column = 0, row = 0)
        self.userName = StringVar()
        userLabel = ttk.Entry(self.login, textvariable = self.userName, width = "30", font = "10")
        userLabel.grid(column = 0, row = 1)

        style = ttk.Style()
        style.configure("TEntry", background = "green")
        ttk.Label(self.login, text = "Password", font = "10", justify = "center").grid(column = 0, row = 2)
        self.passWord = StringVar()
        passLabel   = ttk.Entry(self.login, textvariable = self.passWord, width = "30", font = "10", show="*")
        passLabel   .grid(column = 0, row = 3)

        #loginButton = Button(self.login, text = "Log in", font = "8",
        #                    borderwidth = 1, bg ="white", activeforeground = "green",
        #                    relief = "groove", command = signIn, border = 0)
        #loginButton.grid(column = 0, row = 4)

        crudeImage = Image.open("login.png")
        crudeImage = crudeImage.resize((48,30), Image.ANTIALIAS)

        self.img = ImageTk.PhotoImage(crudeImage)

        button  = Button(self.login, image = self.img, command = signIn, border = 0)
        button  .grid(column = 0, row = 4)

        userLabel.bind('<Return>', signIn)
        passLabel.bind('<Return>', signIn)

        for child in self.login.winfo_children():
            child.grid_configure(padx = 35, pady = 5)
      
    def draw(self):
        self.login.grid(column = 0, row = 0, sticky = (N, W, E, S))
    
    def forget(self):
        self.login.grid_forget()