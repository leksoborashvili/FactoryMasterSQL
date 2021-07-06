from tkinter import ttk
from tkinter import *


class Packaging:
    
    def __init__(self, root):
        self.packagingframe = ttk.Frame(root, padding = "3 3 12 12")
        x = 0
        k = 1
        for i in range (0, 17):
            ttk.Label(self.packagingframe, text = self.packagingList[i]).grid(column = k, row = x-x%2, sticky = W)
            self.packagingValues.append(StringVar())
            entry = ttk.Entry(self.packagingframe, width = 20, font = "10", textvariable = self.packagingValues[i])
            entry.grid(column = k+1, row = x-x%2, sticky = W)
            x+=1
            k= (k*3)%4

        
        for child in self.packagingframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)


    packagingList = [ "EachHeight", "EachWidth", "EachDepth", "InnerHeight", "InnerWidth", "InnerDepth",
                "CaseHeight", "CaseWidth", "CaseDepth", "CaseCube", "PalletHeight", "PalletWidth", "PalletDepth", 
                "PackagingDieline", "PackagingSpec", "CaseDieline", "PalletConfig" ]

    packagingValues = []

    def setValues(self, data):
        for i in range(0, 17):
            self.packagingValues[i].set(data[i])

    def draw(self):
        self.packagingframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

    def forget(self):
        self.packagingframe.grid_forget()





