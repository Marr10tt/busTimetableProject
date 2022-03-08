from tkinter import *
from tkinter import ttk 

def generateTable(tableheight, tableWidth, tablex, tabley):
    tableFrame = Frame()
    tableFrame.place(relx=tablex, rely=tabley, anchor=CENTER)

    timetable = ttk.Treeview()