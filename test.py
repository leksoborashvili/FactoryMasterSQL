from tkinter import *
from tkinter import filedialog
from base64	import *
import base64
import io
from PIL import  Image, ImageTk
import pyodbc

class Img:

	def __init__(self):
		self.server = 'factorydataserver.database.windows.net'
		self.database = 'DataBase1'
		self.username = 'Kpursell'
		self.password = 'F@ct0ry315'
		self.driver= '{ODBC Driver 17 for SQL Server}'
		with pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password) as conn:
			self.con = conn
		self.cursor = self.con.cursor()
		


	def openImage(self):
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
		print(email)
		print(photo_bytes)
		self.cursor.execute("INSERT INTO [dbo].[validation] VALUES (?, ?)", email, photo_bytes)
		self.cursor.commit()

	def selectImage(self):
		self.cursor.execute("SELECT photo FROM [dbo].[validation]")
		data  = self.cursor.fetchone()[0]

		crudeImg = Image.open(io.BytesIO(data))
		crudeImg = crudeImg.resize((300,150), Image.ANTIALIAS)
		self.img = ImageTk.PhotoImage(crudeImg)

		canvas = Label(root, image = self.img)
		canvas.grid(column = 0,  row = 2, rowspan = 3)

		image_result = open('written.png', 'wb')
		image_result.write(data)
		image_result.close()


root = Tk()
img = Img()
root.geometry("300x200")
button  = Button(root, text = "SELECT",
				command = lambda: img.selectImage(),
				border = 0)
button  .grid(column = 0, row = 1)


root.mainloop()