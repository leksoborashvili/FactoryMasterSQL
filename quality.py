from tkinter import ttk
from tkinter import *

class Quality:

    def __init__(self, root):
        self.qualityframe = ttk.Frame(root, padding = "3 3 12 12")
        x = 0
        for i in range (0, 15):
            ttk.Label(self.qualityframe, text = self.qualityList[i]).grid(column = 1, row = x, sticky = W)
            self.qualityValues.append(StringVar())
            entry = ttk.Entry(self.qualityframe, width = 20, textvariable = self.qualityValues[i])
            entry.grid(column = 2, row = x, sticky = W)
            x+=1

        for child in self.qualityframe.winfo_children():
            child.grid_configure(padx = 5, pady = 5)



    qualityList = [ 'CountryOfOriginName', 'CodeDateExample', 'CodeDateFormula', 'CodeDateType', 'CodeDateStamp',
            'ShelfLifeDaysGuarantee', 'ShelfLifeDaysAtProduction', 'ShippingCondition', 'StorageCondition',
            'ShippingTemperatureRangeHigh', 'ShippingTemperatureRangeLow', 'StorageTemperatureRangeHigh', 
            'StorageTemperatureRangeLow', 'NFP', 'Ingredients']

    qualityValues = []


    
    def setValues(self, data):
        for i in range(0, 15):
            self.qualityValues[i].set(data[i])

    def draw(self):
        self.qualityframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

    def forget(self):
        self.qualityframe.grid_forget()
