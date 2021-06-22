from tkinter import *
from tkinter import ttk


class Supply:

    def __init__(self,root):
        self.supplyframe = ttk.Frame(root, padding = "3 3 12 12")

        x = 0
        for i in range(0, 6):
            ttk.Label(self.supplyframe, text = self.supplyList[i]).grid(column = 1, row = x, sticky = W)
            self.supplyValues.append(StringVar())
            entry = ttk.Entry(self.supplyframe, width = 20, textvariable = self.supplyValues[i])
            entry.grid(column = 2, row = x, sticky = W)
            x+=1

        for child in self.supplyframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)


    supplyList =	['MinOrderCases', 'Warehouse', 'PalletPickPriority',
				'FreightClass', 'NMFC,', 'Manufacturer']
    supplyValues = []

    def setValues(self, data):
        for i in range(0, 6):
            self.supplyValues[i].set(data[i])

    def draw(self):
        self.supplyframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

    def forget(self):
        self.supplyframe.grid_forget()