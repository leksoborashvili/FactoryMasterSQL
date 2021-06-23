from tkinter import *
from tkinter import ttk

class Login:

    def __init__(self, root, signIn):
        self.login = ttk.Frame(root)

        ttk.Label(self.login, text = "Username", font = "10", justify = "center").grid(column = 0, row = 0)
        userName = StringVar()
        ttk.Entry(self.login, textvariable = userName, font = "10").grid(column = 0, row = 1)

        style = ttk.Style()
        style.configure("TEntry", background = "green")
        ttk.Label(self.login, text = "Password", font = "10", justify = "center").grid(column = 0, row = 2)
        passWord = StringVar()
        ttk.Entry(self.login, textvariable = passWord, font = "10", show="*").grid(column = 0, row = 3)

        loginButton = Button(self.login, text = "Log in", font = "8",
                            borderwidth = 1, bg ="white", activeforeground = "green",
                            relief = "groove", command = signIn)
        loginButton.grid(column = 0, row = 4)
        for child in self.login.winfo_children():
            child.grid_configure(padx = 35, pady = 5)
      
    def draw(self):
        self.login.grid(column = 0, row = 0, sticky = (N, W, E, S))
    
    def forget(self):
        self.login.grid_forget()