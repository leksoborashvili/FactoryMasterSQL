from tkinter import *
from tkinter import ttk

class Profile:
    def __init__(self, root, db, data, goBack):

        self.root = root
        self.profileframe = ttk.Frame(self.root, padding = "3 3 12 12")
        self.db = db
        self.data = data
        welcometext = data["displayName"] + "'s profile"
        helloLabel = Label(self.profileframe, text = welcometext, font = 5)
        helloLabel.grid(column = 0, row = 0)

        if (self.db.getUserByEmail(data['mail'])[1] == "ADMIN"):
           self.userView()
        

        goBackButton = ttk.Button(self.profileframe, text = "Go Back", command = goBack)
        goBackButton.grid(column = 0, row = 2)

    def userView(self):
        self.listbox = ttk.Treeview(self.profileframe, columns=('user', 'access'),
                                   show = 'headings', padding = "5 5 5 5",
                                   selectmode = 'browse')
        self.listbox.heading('user', text='User')
        self.listbox.column('user', anchor = CENTER)
        self.listbox.heading('access', text="Access")
        self.listbox.column('access', anchor = CENTER, width = 80)
        users = self.db.getUsers()
        
        for user in users:
            self.listbox.insert('', 'end', values=(user[0], user[1]))
        
        self.listbox.grid(column = 0, row = 1)
        self.listbox.bind("<Double-1>", self.onDoubleClick)

    def onDoubleClick(self, event):
        if(self.db.getUserByEmail(self.data['mail'])[1] != 'ADMIN'):
           messagebox.showwarning('Unauthorized Access', 'You do not have right to do this operation!')
           return

        item = self.listbox.selection()[0]
        
        popWindow = Toplevel(self.root)
        userWindow = ttk.Frame(popWindow, padding = "8 10 10 8")
        userWindow.grid(column = 0, row = 0)
        popWindow.title(self.listbox.item(item)["values"][0])

        choices = ["ADMIN", "MARKETING", "SUPPLY", "SALES",
                  "PACKAGING", "QUALITY", "FINANCE", "REGULAR"]
        chosen = StringVar()
        newWindowLabel = ttk.Label(userWindow, text = "Set " + self.listbox.item(item)["values"][0] +
                                   "'s access to:",
                                   justify = "center",
                                   font = '8')
        newWindowLabel.grid(column = 0, row = 0)
        comboBox = ttk.Combobox(userWindow, textvariable = chosen, values = choices)
        comboBox.grid(column = 0, row = 1)

        comboSubmit = ttk.Button(userWindow, text = "Submit", command = lambda: self.submitComboBox(chosen,popWindow))
        comboSubmit.grid(column = 0, row = 2)
        #self.listbox.item(item, values =(self.listbox.item(item)["values"][0], "REGULAR"))



    def submitComboBox(self, selected, window):
        window.destroy()
        item = self.listbox.selection()[0]
        self.db.updateUserRole(self.listbox.item(item)["values"][0], selected.get())
        self.listbox.item(item, values =(self.listbox.item(item)["values"][0], selected.get()))

    def draw(self):
        self.profileframe.grid(column = 0, row = 0, sticky = (N,W,E,S))
    
    def forget(self):
        self.profileframe.grid_forget()



