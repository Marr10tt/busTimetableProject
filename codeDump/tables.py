from tkinter import *
from tkinter import ttk 

tableHeight = 0
tableWidth = 0
tableX = 0
tableY = 0

def tableSettings(height, width, x, y):
    global tableHeight
    global tableWidth
    global tableX
    global tableY
    tableHeight=height
    tableWidth=width
    tableX=x
    tableY=y

def generateTable():
    tableFrame = Frame()
    tableFrame.config(height=tableHeight, width=tableWidth)
    tableFrame.place(relx=tableX, rely=tableY, anchor=CENTER)

    timetable = ttk.Treeview(tableFrame)
    timetable['columns']= ('1', '2')

    timetable.column("#0", width=0, stretch=NO)
    timetable.column("1", width=100, anchor=CENTER)
    timetable.column("2", width=600, anchor=W)

    timetable.heading("#0", text="")
    timetable.heading("#1", text="route number")
    timetable.heading("#2", text="route name")

    timetable.insert(parent='', index='end', iid=1, text="", values=("73", "Lakeside circular"))
    timetable.insert(parent='', index='end', iid=2, text="", values=("72", "Lakeside circular"))
    timetable.insert(parent='', index='end', iid=3, text="", values=("81", "Armthorpe circular"))

    timetable.pack()