from tkinter import *
from tkinter import ttk 
import distanceCalculator
import os
import webbrowser
import routeScreen

tableHeight = 0
tableWidth = 0
tableX = 0
tableY = 0

selectedRoute = ""

def tableSettings(height, width, x, y):
    global tableHeight
    global tableWidth
    global tableX
    global tableY
    tableHeight=height
    tableWidth=width
    tableX=x
    tableY=y

def generateTable(pageName):
    routeList = open('routeList.txt', 'r')
    content=routeList.readlines()

    tableFrame = Frame(pageName)
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

    def OnDoubleClick(self):
        global selectedRoute
        distanceCalculator.coordGet("Bawtry Road")
        distanceCalculator.routing()
        selectedItem = timetable.focus()
        selectedRoute = timetable.item(selectedItem, "values")[0]
        routeScreen.routeNumber=selectedRoute
        pageName.destroy()
        routeScreen.__main__()

    timetable.bind("<Double-1>", OnDoubleClick)

    i=0

    while i<(len(content)-1) and i<20:
        timetable.insert(parent='', index='end', iid=i+1, text="", values=(content[i], content[i+1]))
        i+=2
    timetable.pack()

    '''
    for i in range(0, len(content)):
        timetable.insert(parent='', index='end', iid=i+1, text="", values=(content[i], content[i+1]))
    '''