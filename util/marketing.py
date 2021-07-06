import pyodbc
from tkinter import *
from tkinter import ttk

class Marketing:

    def __init__(self, root):
        self.marketingframe = ttk.Frame(root, padding = "30 3 30 15")
        x = 0
        for i in range(0,15):
            ttk.Label(self.marketingframe, text = self.marketingList[i]).grid(column = 1, row = x, sticky = W)
            self.marketingValues.append(StringVar())
            entry = ttk.Entry(self.marketingframe, width = 20, font = "10", textvariable = self.marketingValues[i])
            entry.grid(column = 2, row = x, sticky = W)
            x+=1

        for i in range(15,29):
            ttk.Label(self.marketingframe, text = self.marketingList[i]).grid(column = 3, row = x-15, sticky = W)
            self.marketingValues.append(StringVar());
            entry = ttk.Entry(self.marketingframe, width = 20, font = "10", textvariable = self.marketingValues[i])
            entry.grid(column = 4, row = x-15, sticky = W)
            x+=1

        for child in self.marketingframe.winfo_children(): 
            child.grid_configure(padx = 5, pady = 5)


    

    marketingList = ["Format", "FoodServiceBulkPack", "EachUPC",
                "EachWeight", "EachUOM", "QtyPerInner",
                "InnerPackUPC", "InnerWeight", "InnerUOM",
                "QtyPerCase", "CaseUPC", "CaseWeight", "CaseUOM",
                "QtyCasesperPallet", "CaseGTIN", "Short Description",
                "Long Description", "FrontImage", "RearImage",
                "Layflat", "Perishable", "IsMultiPack", "IsVarietyPack",
                "IsDisplayShipper", "PalletUPC", "PalletWeight",
                "PalletUOM", "PalletTi", "PalletHi"]
    marketingValues = []

    def setValues(self, data):
        for i in range(0,29):
            self.marketingValues[i].set(data[i])

    def draw(self):
        self.marketingframe.grid(column = 0, row = 2, sticky=(N, W, E, S))

    def forget(self):
        self.marketingframe.grid_forget()