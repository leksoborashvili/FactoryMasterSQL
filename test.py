from tkinter import *
from tkinter import filedialog
from PIL import  Image, ImageTk
import pyodbc

class Img:

	def openImage(self,cursor):
		imageLocation = filedialog.askopenfilename(initialdir = "/",title = "Select file",
													 filetypes = (("jpeg files","*.jpg"),("png files", "*.png"),("all files","*.*")))
	
		crudeImage = Image.open(imageLocation)
		crudeImage = crudeImage.resize((300,150), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(crudeImage)
		canvas = Label(root, image = self.img)
		canvas.grid(column = 0,  row = 2, rowspan = 3)
		with open(imageLocation, 'rb') as photo_file:
			photo_bytes = photo_file.read()
		email = "test"
		cursor.execute("INSERT INTO [dbo].[validation] (email, photo) VALUES (?, ?)", email, photo_bytes)

server = 'factorydataserver.database.windows.net'
database = 'DataBase1'
username = 'Kpursell'
password = 'F@ct0ry315'
driver= '{ODBC Driver 17 for SQL Server}'
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    con = conn
cursor = con.cursor()

root = Tk()
img = Img()
root.geometry("300x200")
button  = Button(root, text = "SELECT",
				command = lambda: img.openImage(cursor),
				border = 0)
button  .grid(column = 0, row = 1)


root.mainloop()