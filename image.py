import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import  Image, ImageTk


class Img(object):
    def __init__(self, root):
        self.imageframe = ttk.Frame(root, padding = (30,10,30,15))
        imageButton = ttk.Button(self.imageframe, text = "Select Image", command = self.onClickHandle)
        imageButton.grid(column = 1, row = 1)

    def onClickHandle(self):
        imageLocation = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                   filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("png files", "*.png")))
        crude = Image.open(imageLocation)
        crude = crude.resize((300,150), Image.ANTIALIAS)
        self.setImage(crude)
        #saves current image as bytes
        with open(imageLocation, 'rb') as photo_file:
            self.photo_bytes = photo_file.read()

    def setImage(self, image):
        self.image = ImageTk.PhotoImage(image)
        canvas = Label(self.imageframe, image = self.image)
        canvas.grid(column = 2,  row = 1, rowspan = 3)

    def show(self):
        self.imageframe.grid(column = 0, row = 2, sticky=(N, W, E, S))

    def forget(self):
        self.imageframe.grid_forget()



