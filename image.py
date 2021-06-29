import pyodbc
from tkinter import *
from tkinter import ttk
from PIL import  Image, ImageTk


class Img(object):
    def __init__(self, root):
        self.imageframe = ttk.Frame(root, padding = (30,3,30,15))


    def setImage(self, image):
        self.image = ImageTk.PhotoImage(image)
        canvas = Label(self.imageframe, image = self.image)
        canvas.grid(column = 0,  row = 0, rowspan = 3)

    def show(self):
        self.imageframe.grid(column = 0, row = 2, sticky=(N, W, E, S))

    def forget(self):
        self.imageframe.grid_forget()



