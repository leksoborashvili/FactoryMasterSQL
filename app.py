from tkinter import *
from tkinter import ttk
from loginwindow import Login
from mainWindow import MW
from auth import Authorization



class App:

    def signIn(self, event = None):
        if(auth.authorize(login.userName.get(), login.passWord.get(), self.failedLogin)):
            login.forget()
            login.passWord.set("")
            mw.draw()
        
    def failedLogin(self,errorMessage):
        errorWindow = Toplevel(root)
        errorLabel  = ttk.Label(errorWindow, text = errorMessage, font = "8")
        errorLabel.grid(column = 0, row = 0)

    def logout(self):
        mw.forget()
        login.draw()




app = App()

auth = Authorization()

root = Tk();
root.title('Database Manager')
login = Login(root,app.signIn)
login.draw()

mw = MW(root, app.logout)
#mw.draw()



root.mainloop()



