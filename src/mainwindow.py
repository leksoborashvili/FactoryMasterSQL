from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from PIL import  Image, ImageTk
import requests
import json
from functools import partial
from util.databaseConnector import DB
from util.marketing import Marketing
from util.supply import Supply
from util.sales import Sales
from util.packaging import Packaging
from util.quality import Quality
from util.finance import Finance
from util.image import Img
from profile import Profile


class MW:
    def __init__(self, root, logout, token):

        self.token = token
        self.root = root
        #self.root.geometry('400x500')
        self.db = DB()
        self.firstframe = Frame(root)
        self.firstframe.pack(fill = BOTH, expand = 1)

        mainCanvas = Canvas(self.firstframe, width = 880, height = (root.winfo_screenheight()*8/10))
        mainCanvas.pack(side = LEFT, fill=BOTH, expand=1)

        mainScroll = ttk.Scrollbar(self.firstframe, orient = VERTICAL, command = mainCanvas.yview)
        mainScroll.pack(side=RIGHT, fill=Y)

        mainCanvas.configure(yscrollcommand = mainScroll.set)
        mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion = mainCanvas.bbox("all")))

        self.mainframe = Frame(mainCanvas)
        
        mainCanvas.create_window((0,0), window = self.mainframe, anchor = "nw")


        self.navigationLabels = ttk.Frame(self.mainframe, padding="3 3 12 12")
        self.navigationLabels.grid(column = 0, row = 0, sticky=(N, W, E, S))

        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)

        #creating navigation top labels
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

        crudeImage = Image.open("media/logo.png")
        crudeImage = crudeImage.resize((300,150), Image.ANTIALIAS)
        self.setImage(crudeImage)

        #profile section code
        self.drawProfile(logout)

        
        #logoutButton    .grid_configure(padx = 50, pady = 10)

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
        privilege = self.db.getUserByEmail(self.user[0])[1]
        if (self.curState.get() == "marketing" and (privilege == "MARKETING" or privilege == "ADMIN")):
            if(not(privilege == "MARKETING" or privilege == "ADMIN")):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.marketing.marketingValues)
            self.db.insertIntoMarketing(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "supply"):
            if(not((privilege == "SUPPLY" or privilege == "ADMIN"))):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.supply.supplyValues)
            self.db.insertIntoSupplyPlanning(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "sales"):
            if(not((privilege == "SALES" or privilege == "ADMIN"))):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.sales.salesValues)
            self.db.insertIntoSales(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "packaging"):
            if(not((privilege == "PACKAGING" or privilege == "ADMIN"))):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.packaging.packagingValues)
            self.db.insertIntoPackaging(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "quality"):
            if(not((privilege == "QUALITY" or privilege == "ADMIN"))):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.quality.qualityValues)
            self.db.insertIntoQuality(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "finance"):
            if(not((privilege == "FINANCE" or privilege == "ADMIN"))):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            values = map(lambda x: x.get(), self.finance.financeValues)
            self.db.insertIntoFinance(brand, pStyleName, pFlavorName, values)

        if (self.curState.get() == "image" and (privilege != "REGULAR")):
            if (privilege == "REGULAR"):
                messagebox.showwarning('Error', "You dont have authority!")
                return
            self.db.insertPhoto(brand, pStyleName, pFlavorName, self.image.photo_bytes)

    def marketingOnClick(self):
        self.deselectAll()
        self.marketingButton.select()
        
        self.curState    .set("marketing")
        self.forgetAll()
        self.marketing   .draw()


    def supplyOnClick(self):
        self.deselectAll()
        self.supplyButton.select()
        self.curState     .set("supply")
        self.forgetAll()
        self.supply       .draw()

    def salesOnClick(self):
        self.deselectAll()
        self.salesButton.select()
        self.curState    .set("sales")
        self.forgetAll()
        self.sales       .draw()

    def packagingOnClick(self):
        self.deselectAll()
        self.packagingButton.select()
        self.curState    .set("packaging")
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .forget()
        self.packaging   .draw()

    def qualityOnClick(self):
        self.deselectAll()
        self.qualityButton.select()
        self.curState    .set("quality")
        self.forgetAll()
        self.quality     .draw()

    def financeOnClick(self):
        self.deselectAll()
        self.financeButton.select()
        self.curState    .set('finance')
        self.forgetAll()
        self.finance     .draw()

    def imageOnClick(self):
        self.deselectAll()
        self.curState    .set('image')
        self.forgetAll()
        self.image       .show()

        self.imageButton.select()
        

    def deselectAll(self):
        self.imageButton.deselect()
        self.marketingButton.deselect()
        self.supplyButton.deselect()
        self.salesButton.deselect()
        self.packagingButton.deselect()
        self.qualityButton.deselect()
        self.financeButton.deselect()

    def forgetAll(self):
        self.marketing   .forget()
        self.supply      .forget()
        self.sales       .forget()
        self.packaging   .forget()
        self.quality     .forget()
        self.finance     .forget()
        self.image       .forget()

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

    def drawProfile(self, logout):
        graph_data = requests.get(
                "https://graph.microsoft.com/v1.0/me/",
                headers={'Authorization': 'Bearer ' + self.token}).json()
        self.user = self.db.getUserByEmail(graph_data['mail'])

        profileframe = ttk.Frame(self.navigationLabels, style = 'profileframe.TFrame')
        profileframe.grid(column = 7, row = 1, rowspan = 3, sticky = N)
        
        prof = Image.open("media/profile.jpg")
        prof = prof.resize((75,75), Image.ANTIALIAS)
        self.profilePic = ImageTk.PhotoImage(prof)
        canvas = Button(profileframe, image = self.profilePic,
                       pady = 0, border = 1, relief = RAISED,
                       command = lambda: self.onProfileClick(graph_data)
                       )
        canvas.grid(column = 0,  row = 0)
 
        #fontUserName = font.Font(family = 'Helvetica', size = 13)
        username = Label(profileframe, text = graph_data["displayName"], font =13)
        username.grid(column = 0, row = 1)
        
        fontRightLabel = font.Font(family = 'Helvetica', size = 10)
        rightLabel = Label(profileframe, text = self.user[1], font = fontRightLabel)
        rightLabel.grid(column = 0, row = 2)

        logoutButton    = ttk.Button(profileframe, text = "Logout", command = logout)
        logoutButton    .grid(column = 0, row = 3)


    def onProfileClick(self, graph_data):
        self.profile = Profile(self.root, self.db, graph_data, self.leaveProfileWindow)
        self.forget()
        self.profile.draw()

    def leaveProfileWindow(self):
        self.profile.forget()
        self.draw()

    def draw(self):
        self.firstframe.grid(column = 0, row = 0, sticky=(N, W, E, S))
    
    def forget(self):
        self.firstframe.grid_forget()