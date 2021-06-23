from tkinter import *
from tkinter import ttk
from loginwindow import Login
from mainWindow import MW

def signIn():
    login.forget()
    mw.draw()


root = Tk();
root.title('Database Manager')
login = Login(root,signIn)
login.draw()

mw = MW(root)
#mw.draw()



root.mainloop()



