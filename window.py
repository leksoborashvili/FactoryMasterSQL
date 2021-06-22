from tkinter import *
from tkinter import ttk
from databaseConnector import DB


db = DB()
#retrieve button command
def retrieve():
    brand       = bName.get()
    pStyleName  = productStyleName.get()
    pFlavorName = productFlavorName.get()
    data = []
    if (curState.get() == "marketing"):
        data = db.selectMarketing(brand, pStyleName, pFlavorName)
        for i in range(0,29):
            marketingValues[i].set(data[i])

    if (curState.get() == "supply"):
        data = db.selectSupplyPlanning(brand, pStyleName, pFlavorName)
        for i in range(0, 6):
            supplyValues[i].set(data[i])

    if (curState.get() == "sales"):
        data = db.selectSales(brand, pStyleName, pFlavorName)
        for i in range(0, 6):
            salesValues[i].set(data[i])

    if (curState.get() == "packaging"):
        data = db.selectPackaging(brand, pStyleName, pFlavorName)
        for i in range(0, 17):
            packagingValues[i].set(data[i])

    if (curState.get() == "quality"):
        data = db.selectQuality(brand, pStyleName, pFlavorName)
        for i in range(0, 15):
            qualityValues[i].set(data[i])

    if (curState.get() == "finance"):
        data = db.selectFinance(brand, pStyleName, pFlavorName)
        for i in range(0, 3):
            financeValues[i].set(data[i])


#update button command
def update():
    brand       = bName.get()
    pStyleName  = productStyleName.get()
    pFlavorName = productFlavorName.get()

    if (curState.get() == "marketing"):
        values = map(lambda x: x.get(), marketingValues)
        db.insertIntoMarketing(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "supply"):
        values = map(lambda x: x.get(), supplyValues)
        db.insertIntoSupplyPlanning(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "sales"):
        values = map(lambda x: x.get(), salesValues)
        db.insertIntoSales(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "packaging"):
        values = map(lambda x: x.get(), packagingValues)
        db.insertIntoPackaging(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "quality"):
        values = map(lambda x: x.get(), qualityValues)
        db.insertIntoQuality(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "finance"):
        values = map(lambda x: x.get(), financeValues)
        db.insertIntoFinance(brand, pStyleName, pFlavorName, values)


def marketingOnClick():
    curState.set("marketing")
    supplyframe.grid_forget()
    marketingframe.grid_forget()
    packagingframe.grid_forget()
    qualityframe.grid_forget()
    financeframe.grid_forget()
    marketingframe .grid(column = 0, row = 2, sticky=(N, W, E, S))

def supplyOnClick():
   curState.set("supply")
   marketingframe.grid_forget()
   salesframe.grid_forget()
   packagingframe.grid_forget()
   qualityframe.grid_forget()
   financeframe.grid_forget()
   supplyframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

def salesOnClick():
    curState.set("sales")
    marketingframe.grid_forget()
    supplyframe.grid_forget()
    packagingframe.grid_forget()
    qualityframe.grid_forget()
    financeframe.grid_forget()
    salesframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

def packagingOnClick():
    curState.set("packaging")
    marketingframe.grid_forget()
    supplyframe.grid_forget()
    salesframe.grid_forget()
    qualityframe.grid_forget()
    financeframe.grid_forget()
    packagingframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

def qualityOnClick():
    curState.set("quality")
    marketingframe.grid_forget()
    supplyframe.grid_forget()
    salesframe.grid_forget()
    packagingframe.grid_forget()
    financeframe.grid_forget()
    qualityframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

def financeOnClick():
    curState.set('finance')
    marketingframe.grid_forget()
    supplyframe.grid_forget()
    salesframe.grid_forget()
    packagingframe.grid_forget()
    financeframe.grid(column = 0, row = 2, sticky = (N, W, E, S))

root = Tk();
root.title('Database Manager')

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)



# creating navigation top labels

brandName           = ttk.Label(mainframe, text="BrandName")
brandName           .grid(column=1,row=1, sticky = W)
bName               = StringVar()
brandName_entry     = ttk.Entry(mainframe, width = 20, textvariable = bName)
brandName_entry     .grid(column = 2, row = 1, sticky = W)

productStyle        = ttk.Label(mainframe, text="ProductStyle/Category")
productStyle        .grid(column = 1, row = 2, sticky = W);
productStyleName    = StringVar()
productStyle_entry  = ttk.Entry(mainframe, width = 20, textvariable = productStyleName)
productStyle_entry  .grid(column = 2, row = 2, sticky = W)

productFlavor       = ttk.Label(mainframe, text = "ProductFlavor")
productFlavor       .grid(column = 1, row = 3, sticky = W)
productFlavorName   = StringVar()
productFlavor_entry = ttk.Entry(mainframe, width = 20, textvariable = productFlavorName)
productFlavor_entry .grid(column = 2, row = 3, sticky = W)



# switch button frames
curState = StringVar()
curState.set("marketing")
buttonFrame         = ttk.Frame(root)
buttonFrame         .grid(column = 0, row = 1, sticky=(N, W, E, S))

marketingButton     = ttk.Button(buttonFrame, text = "Marketing", command = marketingOnClick)
marketingButton     .grid(column = 0, row = 1, sticky = W)

supplyButton        = ttk.Button(buttonFrame, text = "Supply", command = supplyOnClick)
supplyButton        .grid(column = 1, row = 1, sticky = W)

salesButton         = ttk.Button(buttonFrame, text = "Sales", command = salesOnClick)
salesButton         .grid(column = 2, row = 1, sticky = W)

packagingButton     = ttk.Button(buttonFrame, text = "Packaging", command = packagingOnClick)
packagingButton     .grid(column = 3, row = 1, sticky = W)

qualityButton       = ttk.Button(buttonFrame, text = "Quality", command = qualityOnClick)
qualityButton       .grid(column = 4, row = 1, sticky = W)

financeButton       = ttk.Button(buttonFrame, text = "Finance", command = financeOnClick)
financeButton       .grid(column = 5, row = 1, sticky = W)


#Displaying marketing section
marketingframe = ttk.Frame(root, padding = "3 3 12 12")
marketingframe .grid(column = 0, row = 2, sticky=(N, W, E, S))

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

x = 0
for i in range(0,15):
    ttk.Label(marketingframe, text = marketingList[i]).grid(column = 1, row = x, sticky = W)
    marketingValues.append(StringVar())
    entry = ttk.Entry(marketingframe, width = 20, textvariable = marketingValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1

for i in range(15,29):
    ttk.Label(marketingframe, text = marketingList[i]).grid(column = 3, row = x-15, sticky = W)
    marketingValues.append(StringVar());
    entry = ttk.Entry(marketingframe, width = 20, textvariable = marketingValues[i])
    entry.grid(column = 4, row = x-15, sticky = W)
    x+=1



#displaying supply planning window
supplyframe = ttk.Frame(root, padding = "3 3 12 12")

supplyList =	['MinOrderCases', 'Warehouse', 'PalletPickPriority',
				'FreightClass', 'NMFC,', 'Manufacture']
supplyValues = []
x = 0
for i in range(0, 6):
    ttk.Label(supplyframe, text = supplyList[i]).grid(column = 1, row = x, sticky = W)
    supplyValues.append(StringVar())
    entry = ttk.Entry(supplyframe, width = 20, textvariable = supplyValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1

#displaying sales window
salesframe = ttk.Frame(root, padding = "3 3 12 12")

salesList =  ['DistributorDeliveredCasePrice', 'SRP', 'PlanogramDepth', 'PlanogramHeight', 'PlanogramWidth', 'VendorSKU']

salesValues = []
x = 0
for i in range(0, 6):
    ttk.Label(salesframe, text = salesList[i]).grid(column = 1, row = x, sticky = W)
    salesValues.append(StringVar())
    entry = ttk.Entry(salesframe, width = 20, textvariable = salesValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1

#displaying Packaging engineering window
packagingframe = ttk.Frame(root, padding = "3 3 12 12")

packagingList = [ "EachHeight", "EachWidth", "EachDepth", "InnerHeight", "InnerWidth", "InnerDepth",
            "CaseHeight", "CaseWidth", "CaseDepth", "CaseCube", "PalletHeight", "PalletWidth", "PalletDepth", 
            "PackagingDieline", "PackagingSpec", "CaseDieline", "PalletConfig" ]

packagingValues = []

x = 0
for i in range (0, 17):
    ttk.Label(packagingframe, text = packagingList[i]).grid(column = 1, row = x, sticky = W)
    packagingValues.append(StringVar())
    entry = ttk.Entry(packagingframe, width = 20, textvariable = packagingValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1

#displaying quality window
qualityframe = ttk.Frame(root, padding = "3 3 12 12")

qualityList = [ 'CountryOfOriginName', 'CodeDateExample', 'CodeDateFormula', 'CodeDateType', 'CodeDateStamp',
            'ShelfLifeDaysGuarantee', 'ShelfLifeDaysAtProduction', 'ShippingCondition', 'StorageCondition',
            'ShippingTemperatureRangeHigh', 'ShippingTemperatureRangeLow', 'StorageTemperatureRangeHigh', 
            'StorageTemperatureRangeLow', 'NFP', 'Ingredients']

qualityValues = []

x = 0
for i in range (0, 15):
    ttk.Label(qualityframe, text = qualityList[i]).grid(column = 1, row = x, sticky = W)
    qualityValues.append(StringVar())
    entry = ttk.Entry(qualityframe, width = 20, textvariable = qualityValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1

#displaying finance window
financeframe = ttk.Frame(root, padding = "3 3 12 12")

financeList = [ 'UnitCost', 'CaseCost', 'Internal Item Numberr' ]

financeValues = []

x = 0
for i in range (0, 3):
    ttk.Label(financeframe, text = financeList[i]).grid(column = 1, row = x, sticky = W)
    financeValues.append(StringVar())
    entry = ttk.Entry(financeframe, width = 20, textvariable = financeValues[i])
    entry.grid(column = 2, row = x, sticky = W)
    x+=1


#retrieve button
commandButtonframe = ttk.Frame(root)
commandButtonframe . grid(column = 0, row = 3, sticky = (N, W, E, S))

retrieveButton  =  ttk.Button(commandButtonframe, text = "Retrieve", command = retrieve)
retrieveButton.grid(column = 0, row = 0, sticky = W)
retrieveButton.grid_configure(padx = 20, pady = 10)

updateButton    = ttk.Button(commandButtonframe, text = "Update", command = update)
updateButton.grid(column = 2, row = 0, sticky = W)
retrieveButton.grid_configure(padx = 20, pady = 10)

# padding every element in the frames
for child in mainframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

for child in marketingframe.winfo_children(): 
    child.grid_configure(padx = 5, pady = 5)

for child in supplyframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

for child in salesframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

for child in packagingframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

for child in qualityframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)

for child in financeframe.winfo_children():
    child.grid_configure(padx = 5, pady = 5)


root.mainloop()
