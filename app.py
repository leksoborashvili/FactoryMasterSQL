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
            self.mw = MW(root, app.logout)
            self.mw.draw()
        
    def failedLogin(self,errorMessage):
        errorWindow = Toplevel(root)
        errorLabel  = ttk.Label(errorWindow, text = errorMessage, font = "8")
        errorLabel.grid(column = 0, row = 0)

    def logout(self):
        self.mw.forget()
        login.draw()
        auth.logout()




app = App()
auth = Authorization()

root = Tk();
root.title('Database Manager')

login = Login(root,app.signIn)
login.draw()


#mw.draw()



root.mainloop()



