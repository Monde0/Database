from tkinter import *
from PIL import Image, ImageTk 

class user():
    def __init__(self):

        self.cwin = Toplevel()

        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\user2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="User ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="User FName: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="User LName: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="User Phone: ")
        self.empStaEn = Entry(bdF)

        self.empEm = Label(bdF, text="User Email: ")
        self.empEmEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1,pady=5)
        self.empAge.grid(row=2,column=0)
        self.empAgeEn.grid(row=2,column=1,pady=5)
        self.empSta.grid(row=3,column=0)
        self.empStaEn.grid(row=3,column=1,pady=5)
        self.empEm.grid(row=4,column=0)
        self.empEmEn.grid(row=4,column=1,pady=5)


        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Query User')
        self.cwin.geometry('450x450')

class roomer():
    def __init__(self):

        self.cwin = Toplevel()

        topFrame = Frame(self.cwin, pady=30)

        C = Canvas(self.cwin, bg="blue", height=50, width=50)
        filename = PhotoImage(file = "C:\\Users\\USER\\Desktop\\USE\\Year3\\database\\work\\images\\user2.png")
       
        background_label = Label(self.cwin, image=filename)
        background_label.place(x=0, y=-100)

        background_label.image = filename # reference to the image

        background_label.grid(row=0,column=0)

        # body

        bdF = Frame(self.cwin)

        self.empID = Label(bdF, text="Roomer ID: ")
        self.empEn = Entry(bdF)

        self.empName = Label(bdF, text="Roomer FName: ")
        self.empNameEn = Entry(bdF)

        self.empAge = Label(bdF, text="Roomer LName: ")
        self.empAgeEn = Entry(bdF)

        self.empSta = Label(bdF, text="Roomer Phone: ")
        self.empStaEn = Entry(bdF)

        self.empPl = Label(bdF, text="Roomer Email: ")
        self.empPlEn = Entry(bdF)

        self.empID.grid(row=0,column=0)
        self.empEn.grid(row=0,column=1, pady=5)
        self.empName.grid(row=1,column=0)
        self.empNameEn.grid(row=1,column=1,pady=5)
        self.empAge.grid(row=2,column=0)
        self.empAgeEn.grid(row=2,column=1,pady=5)
        self.empSta.grid(row=3,column=0)
        self.empStaEn.grid(row=3,column=1,pady=5)
        self.empPl.grid(row=4,column=0)
        self.empPlEn.grid(row=4,column=1,pady=5)

        bdF.grid(row=1)

        foot = Frame(self.cwin, pady=20)

        self.but = Button(foot, text="SEARCH", width=15)
        self.exit = Button(foot, text="EXIT", width=15, command=self.cwin.destroy)

        self.but.pack(side=LEFT, padx=10)
        self.exit.pack(side=RIGHT)

        foot.grid(row=2)


        self.cwin.title('Query Roomer')
        self.cwin.geometry('450x450')