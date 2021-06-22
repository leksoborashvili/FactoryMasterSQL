from tkinter import ttk
from tkinter import *

class Finance:

    def __init__(self, root):
        self.financeframe = ttk.Frame(root, padding = "3 3 12 12")
        x = 0
        for i in range (0, 3):
            ttk.Label(self.financeframe, text = self.financeList[i]).grid(column = 1, row = x, sticky = W)
            self.financeValues.append(StringVar())
            entry = ttk.Entry(self.financeframe, width = 20, textvariable = self.financeValues[i])
            entry.grid(column = 2, row = x, sticky = W)
            x+=1

        for child in self.financeframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)


        
    financeList = [ 'UnitCost', 'CaseCost', 'Internal Item Numberr' ]

    financeValues = []

    def setValues(self, data):
        for i in range(0, 3):
            self.financeValues[i].set(data[i])

    def draw(self):
        self.financeframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

    def forget(self):
        self.financeframe.grid_forget()

