from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from src.loginwindow import Login
from src.mainwindow import MW
from util.auth import Authorization
import requests
import json


class App:

    def signIn(self, event = None):
        self.user_token = auth.authorize(login.userName.get(), login.passWord.get(), self.failedLogin)
        if(self.user_token):
            login.forget()
            login.passWord.set("")
            self.mw = MW(root, app.logout, self.user_token)
            self.mw.draw()

            graph_data = requests.get(
                "https://graph.microsoft.com/v1.0/me/",
                headers={'Authorization': 'Bearer ' + self.user_token}).json()

            self.mw.db.insertUser(graph_data['mail'], "REGULAR")
        
    def failedLogin(self,errorMessage):
        messagebox.showwarning('Error', errorMessage)

    def logout(self):
        user_token = None
        self.mw.forget()
        login.draw()
        auth.logout()

app = App()
auth = Authorization()

root = Tk()
root.title('Database Manager')

login = Login(root,app.signIn)
login.draw()


#mw.draw()



root.mainloop()



