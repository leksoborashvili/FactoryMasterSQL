from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk
from databaseConnector import DB
from marketing import Marketing
from supply import Supply
from sales import Sales
from packaging import Packaging
from quality import Quality
from finance import Finance
from functools import partial

db = DB()
#retrieve button command
def retrieve():
    brand       = bName.get()
    pStyleName  = productStyleName.get()
    pFlavorName = productFlavorName.get()
    data = []
    if (curState.get() == "marketing"):
        data = db.selectMarketing(brand, pStyleName, pFlavorName)
        marketing.setValues(data)

    if (curState.get() == "supply"):
        data = db.selectSupplyPlanning(brand, pStyleName, pFlavorName)
        supply.setValues(data)
       
    if (curState.get() == "sales"):
        data = db.selectSales(brand, pStyleName, pFlavorName)
        sales.setValues(data)

    if (curState.get() == "packaging"):
        data = db.selectPackaging(brand, pStyleName, pFlavorName)
        packaging.setValues(data)

    if (curState.get() == "quality"):
        data = db.selectQuality(brand, pStyleName, pFlavorName)
        quality.setValues(data)

    if (curState.get() == "finance"):
        data = db.selectFinance(brand, pStyleName, pFlavorName)
        finance.setValues(data)


#update button command
def update():
    brand       = bName.get()
    pStyleName  = productStyleName.get()
    pFlavorName = productFlavorName.get()

    if (curState.get() == "marketing"):
        values = map(lambda x: x.get(), marketing.marketingValues)
        db.insertIntoMarketing(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "supply"):
        values = map(lambda x: x.get(), supply.supplyValues)
        db.insertIntoSupplyPlanning(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "sales"):
        values = map(lambda x: x.get(), sales.salesValues)
        db.insertIntoSales(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "packaging"):
        values = map(lambda x: x.get(), packaging.packagingValues)
        db.insertIntoPackaging(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "quality"):
        values = map(lambda x: x.get(), quality.qualityValues)
        db.insertIntoQuality(brand, pStyleName, pFlavorName, values)

    if (curState.get() == "finance"):
        values = map(lambda x: x.get(), finance.financeValues)
        db.insertIntoFinance(brand, pStyleName, pFlavorName, values)


def marketingOnClick():
    curState.set("marketing")
    supply.forget()
    sales.forget()
    packaging.forget()
    quality.forget()
    finance.forget()
    marketing.draw()

def supplyOnClick():
   curState.set("supply")
   sales.forget()
   packaging.forget()
   quality.forget()
   finance.forget()
   supply.draw()

def salesOnClick():
    curState.set("sales")
    marketing.forget()
    supply.forget()
    packaging.forget()
    quality.forget()
    finance.forget()
    sales.draw()

def packagingOnClick():
    curState.set("packaging")
    marketing.forget()
    supply.forget()
    sales.forget()
    quality.forget()
    finance.forget()
    packaging.draw()

def qualityOnClick():
    curState.set("quality")
    marketing.forget()
    supply.forget()
    sales.forget()
    packaging.forget()
    finance.forget()
    quality.draw()

def financeOnClick():
    curState.set('finance')
    marketing.forget()
    supply.forget()
    sales.forget()
    packaging.forget()
    quality.forget()
    finance.draw()

def createOnClick():
    createPop= Toplevel(root)
    createPopLabel = ttk.Label(createPop, text = "Do you want to add object?  \n" + bName.get() + ' \n'
                              + productStyleName.get() + ' \n' + productFlavorName.get(), font = '12')
    style = ttk.Style()
    style.configure('No.TButton', foreground = 'red', )
    style.configure('Yes.TButton', foreground = 'green')
    createPopNoButton  = ttk.Button(createPop, text = "No", style = 'No.TButton', command = createPop.destroy)
    createPopYesButton = ttk.Button(createPop, text = "Yes", style = 'Yes.TButton', command = lambda: createNewObject(createPop) )
    createPopLabel.grid(row = 0, column = 1, sticky = (N, W, E, S))
    createPopNoButton .grid(row = 1, column = 0)
    createPopYesButton.grid(row = 1, column = 2)
    

def createNewObject(pop):
    pop.destroy()
    brand       = bName.get()
    pStyleName  = productStyleName.get()
    pFlavorName = productFlavorName.get()
    db.createObject(brand, pStyleName, pFlavorName)

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

crudeImage = Image.open("logo.png")
crudeImage = crudeImage.resize((200,100), Image.ANTIALIAS)

img = ImageTk.PhotoImage(crudeImage)
canvas = Label(mainframe, image = img)
canvas.grid(column = 3,  row = 1, rowspan = 3)



# switch button frames
curState = StringVar()
curState.set("marketing")
buttonFrame         = ttk.Frame(root)
buttonFrame         .grid(column = 0, row = 1, sticky=(N, W, E, S))

marketingButton     = ttk.Button(buttonFrame, text = "Marketing",  command = marketingOnClick)
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

createButton        = ttk.Button(buttonFrame, text = "Create", command = createOnClick)
createButton        .grid(column = 6, row = 1, padx = (15,5), sticky = W)

#Displaying marketing section
marketing  = Marketing(root)
marketing.draw()

#displaying supply planning window
supply =  Supply(root)

#displaying sales window
sales = Sales(root)

#displaying Packaging engineering window
packaging = Packaging(root)

#displaying quality window
quality = Quality(root)

#displaying finance window
finance = Finance(root)



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


root.mainloop()
