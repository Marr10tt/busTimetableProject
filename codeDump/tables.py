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

    timetable = ttk.Treeview()