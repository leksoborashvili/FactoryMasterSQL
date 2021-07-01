from tkinter import *
from tkinter import ttk


class Profile:
    def __init__(self, root, data, goBack):

        self.profileframe = ttk.Frame(root, padding = "3 3 12 12")
        
        welcometext = data["displayName"] + "'s profile"
        helloLabel = Label(self.profileframe, text = welcometext, font = 5)
        helloLabel.grid(column = 0, row = 0)

        goBackButton = ttk.Button(self.profileframe, text = "Go Back", command = goBack)
        goBackButton.grid(column = 0, row = 1)

    def draw(self):
        self.profileframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
    
    def forget(self):
        self.profileframe.grid_forget()



