from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import  Image, ImageTk
from databaseConnector import DB
from marketing import Marketing
from supply import Supply
from sales import Sales
from packaging import Packaging
from quality import Quality
from finance import Finance
from functools import partial
from image import Img

class MW:
    def __init__(self, root, logout):

        self.root = root
        self.db = DB()
        self.mainframe = ttk.Frame(root)


        self.navigationLabels = ttk.Frame(self.mainframe, padding="3 3 12 12")
        self.navigationLabels.grid(column = 0, row = 0, sticky=(N, W, E, S))

        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)

        # creating navigation top labels
        fontSize = "10"
        brandName               = ttk.Label(self.navigationLabels, text="BrandName")
        brandName               .grid(column=1,row=1, sticky = W)
        self.bName              = StringVar()
        brandName_entry         = ttk.Entry(self.navigationLabels, width = 20, font = fontSize, textvariable = self.bName)
        brandName_entry         .grid(column = 2, row = 1, sticky = W)

        productStyle            = ttk.Label(self.navigationLabels, text="ProductStyle")
        productStyle            .grid(column = 1, row = 2, sticky = W);
        self.productStyleName   = StringVar()
        productStyle_entry      = ttk.Entry(self.navigationLabels, width = 20, font = fontSize, textvariable = self.productStyleName)
        productStyle_entry      .grid(column = 2, row = 2, sticky = W)

        productFlavor           = ttk.Label(self.navigationLabels, text = "ProductFlavor")
        productFlavor           .grid(column = 1, row = 3, sticky = W)
        self.productFlavorName  = StringVar()
        productFlavor_entry     = ttk.Entry(self.navigationLabels, width = 20, font = fontSize, textvariable = self.productFlavorName)
        productFlavor_entry     .grid(column = 2, row = 3, sticky = W)

        crudeImage = Image.open("logo.png")
        crudeImage = crudeImage.resize((300,150), Image.ANTIALIAS)
        self.setImage(crudeImage)



        

        #switch button styles
        switchStyle = ttk.Style()
        switchStyle.configure('Switch.TButton', foreground = "black", background = "red")

        buttonFrame         = ttk.Frame(self.mainframe)
        buttonFrame         .grid(column = 0, row = 1, sticky=(N, W, E, S))

        # switch button frames
        self.curState = StringVar()
        self.curState.set("marketing")
        self.marketingButton     = Checkbutton(buttonFrame, text = "Marketing",
                                        command = self.marketingOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7,
                                        relief = RAISED
                                        )
        self.marketingButton     .grid(column = 0, row = 1, sticky = W)

        self.supplyButton        = Checkbutton(buttonFrame, text = "Supply",
                                        command = self.supplyOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.supplyButton        .grid(column = 1, row = 1, sticky = W)

        self.salesButton         = Checkbutton(buttonFrame, text = "Sales",
                                        command = self.salesOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.salesButton         .grid(column = 2, row = 1, sticky = W)

        self.packagingButton     = Checkbutton(buttonFrame, text = "Packaging",
                                        command = self.packagingOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.packagingButton     .grid(column = 3, row = 1, sticky = W)

        self.qualityButton       = Checkbutton(buttonFrame, text = "Quality",
                                        command = self.qualityOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.qualityButton       .grid(column = 4, row = 1, sticky = W)

        self.financeButton       = Checkbutton(buttonFrame, text = "Finance",
                                        command = self.financeOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.financeButton       .grid(column = 5, row = 1, sticky = W)

        self.imageButton         = Checkbutton(buttonFrame, text = "Image",
                                        command = self.imageOnClick,
                                        indicatoron = 0,
                                        width = 8,
                                        font = 7
                                        )
        self.imageButton         .grid(column = 6, row = 1, sticky = W)

        createButton        = ttk.Button(buttonFrame, text = "Create", command = self.createOnClick)
        createButton        .grid(column = 7, row = 1, padx = (15,5), sticky = W)

        

        #Displaying marketing section
        self.marketing  = Marketing(self.mainframe)
        self.marketing.draw()
        self.marketingButton.select()
        #displaying supply planning window
        self.supply =  Supply(self.mainframe)
        #displaying sales window
        self.sales = Sales(self.mainframe)
        #displaying Packaging engineering window
        self.packaging = Packaging(self.mainframe)
        #displaying quality window
        self.quality = Quality(self.mainframe)
        #displaying finance window
        self.finance = Finance(self.mainframe)
        #displaying image icon
        self.image   = Img(self.mainframe)


        #retrieve button
        commandButtonframe = ttk.Frame(self.mainframe)
        commandButtonframe . grid(column = 0, row = 3, sticky = (N, W, E, S))

        retrieveButton  =  ttk.Button(commandButtonframe, text = "Retrieve", command = self.retrieve)
        retrieveButton  .grid(column = 0, row = 0, sticky = W)
        retrieveButton  .grid_configure(padx = 20, pady = 10)

        updateButton    = ttk.Button(commandButtonframe, text = "Update", command = self.update)
        updateButton    .grid(column = 2, row = 0, sticky = W)
        retrieveButton  .grid_configure(padx = 20, pady = 10)

        logoutButton    = ttk.Button(commandButtonframe, text = "Logout", command = logout)
        logoutButton    .grid(column = 4, row = 0, sticky = E)
        logoutButton    .grid_configure(padx = 50, pady = 10)

        # padding every element in the frames
        for child in self.navigationLabels.winfo_children(): 
            child.grid_configure(padx = 5, pady = 5)

        #Styling all the labels and buttons.
        labelStyle = ttk.Style()
        labelStyle.configure("TLabel", font = "10")

        buttonStyle = ttk.Style()
        buttonStyle.configure("TButton", font = "8")





        #retrieve button command
    def retrieve(self):
        brand       = self.bName.get()
        pStyleName  = self.productStyleName.get()
        pFlavorName = self.productFlavorName.get()
        data = []
        
        crudeImage = self.db.selectImg(brand, pStyleName, pFlavorName)
        if not crudeImage:
            crudeImage = Image.open("logo.png")
        crudeImage = crudeImage.resize((300,150), Image.ANTIALIAS)
        self.setImage(crudeImage)

        if (self.curState.get() == "marketing"):
            data = self.db.selectMarketing(brand, pStyleName, pFlavorName)
            self.marketing.setValues(data)

        if (self.curState.get() == "supply"):
            data = self.db.selectSupplyPlanning(brand, pStyleName, pFlavorName)
            self.supply.setValues(data)
       
        if (self.curState.get() == "sales"):
            data = self.db.selectSales(brand, pStyleName, pFlavorName)
            self.sales.setValues(data)

        if (self.curState.get() == "packaging"):
            data = self.db.selectPackaging(brand, pStyleName, pFlavorName)
            self.packaging.setValues(data)

        if (self.curState.get() == "quality"):
            data = self.db.selectQuality(brand, pStyleName, pFlavorName)
            self.quality.setValues(data)

        if (self.curState.get() == "finance"):
            data = self.db.selectFinance(brand, pStyleName, pFlavorName)
            self.finance.setValues(data)


    #update button command
    def update(self):
        brand       = self.bName.get()
        pStyleName  = self.productStyleName.get()
        pFlavorName = self.productFlavorName.get()

        if (self.curState.get() == "marketing"):
            values = map(lambda x: x.get(), self.marketing.marketingValues)
            self.db.insertIntoMarketing(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "supply"):
            values = map(lambda x: x.get(), self.supply.supplyValues)
            self.db.insertIntoSupplyPlanning(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "sales"):
            values = map(lambda x: x.get(), self.sales.salesValues)
            self.db.insertIntoSales(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "packaging"):
            values = map(lambda x: x.get(), self.packaging.packagingValues)
            self.db.insertIntoPackaging(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "quality"):
            values = map(lambda x: x.get(), self.quality.qualityValues)
            self.db.insertIntoQuality(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "finance"):
            values = map(lambda x: x.get(), self.finance.financeValues)
            self.db.insertIntoFinance(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "image"):
            self.db.insertPhoto(brand, pStyleName, pFlavorName, self.image.photo_bytes)

    def marketingOnClick(self):
        self.marketingButton.select()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.deselect()
        self.imageButton.deselect()
        self.curState    .set("marketing")
        self.supply      .forget()
        self.sales       .forget()
        self.packaging   .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .forget()
        self.marketing   .draw()


    def supplyOnClick(self):
        self.marketingButton.deselect()
        self.supplyButton.select()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.deselect()
        self.imageButton.deselect()
        self.curState     .set("supply")
        self.sales        .forget()
        self.packaging    .forget()
        self.quality      .forget()
        self.finance      .forget()
        self.image       .forget()
        self.supply       .draw()

    def salesOnClick(self):
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.select()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.deselect()
        self.imageButton.deselect()
        self.curState    .set("sales")
        self.marketing   .forget()
        self.supply      .forget()
        self.packaging   .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .forget()
        self.sales       .draw()

    def packagingOnClick(self):
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.select()
        self.qualityButton.deselect()
        self.financeButton.deselect()
        self.imageButton.deselect()
        self.curState    .set("packaging")
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .forget()
        self.packaging   .draw()

    def qualityOnClick(self):
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.select()
        self.financeButton.deselect()
        self.imageButton.deselect()
        self.curState    .set("quality")
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.packaging   .forget()
        self.finance     .forget()
        self.image       .forget()
        self.quality     .draw()

    def financeOnClick(self):
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.select()
        self.imageButton.deselect()
        self.curState    .set('finance')
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.packaging   .forget()
        self.quality     .forget()
        self.image       .forget()
        self.finance     .draw()

    def imageOnClick(self):
        self.imageButton.deselect()
        
        self.curState    .set('image')
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.packaging   .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .show()
        self.imageButton.select()
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.deselect()


    def createOnClick(self):
        createPop= Toplevel(self.root)
        createPopLabel = ttk.Label(createPop, text = "Do you want to add object?  \n" + self.bName.get() + ' \n'
                                  + self.productStyleName.get() + ' \n' + self.productFlavorName.get(),
                                 justify = "center", font = '10')
        style = ttk.Style()
        style.configure('No.TButton', foreground = 'red', )
        style.configure('Yes.TButton', foreground = 'green')
        createPopNoButton  = ttk.Button(createPop, text = "No", style = 'No.TButton', command = createPop.destroy)
        createPopYesButton = ttk.Button(createPop, text = "Yes", style = 'Yes.TButton', command = lambda: self.createNewObject(createPop) )
        createPopLabel.grid(row = 0, column = 1, sticky = (N, W, E, S))
        createPopNoButton .grid(row = 1, column = 0)
        createPopYesButton.grid(row = 1, column = 2)
    
    def createNewObject(self,pop):
        pop.destroy()
        brand       = self.bName.get()
        pStyleName  = self.productStyleName.get()
        pFlavorName = self.productFlavorName.get()
        self.db.createObject(brand, pStyleName, pFlavorName)

    def setImage(self, img):
        self.img = ImageTk.PhotoImage(img)
        canvas = Label(self.navigationLabels, image = self.img)
        canvas.grid(column = 4,  row = 1, rowspan = 3)

    def draw(self):
        self.mainframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
    
    def forget(self):
        self.mainframe.grid_forget()