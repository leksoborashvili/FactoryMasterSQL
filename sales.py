from tkinter import *
from tkinter import ttk

class Sales: 
    
    def __init__(self,root):
        self.salesframe = ttk.Frame(root, padding = "3 3 12 12")
        x = 0
        for i in range(0, 6):
            ttk.Label(self.salesframe, text = self.salesList[i]).grid(column = 1, row = x, sticky = W)
            self.salesValues.append(StringVar())
            entry = ttk.Entry(self.salesframe, width = 20, font = "10", textvariable = self.salesValues[i])
            entry.grid(column = 2, row = x, sticky = W)
            x+=1
        
        for child in self.salesframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)



    salesList =  ['DistributorDeliveredCasePrice', 'SRP', 'PlanogramDepth', 'PlanogramHeight', 'PlanogramWidth', 'VendorSKU']

    salesValues = []

    def setValues(self, data):
        for i in range(0, 6):
            self.salesValues[i].set(data[i])

    def draw(self):
        self.salesframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

    def forget(self):
        self.salesframe.grid_forget()