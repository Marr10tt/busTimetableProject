import tkinter
from tkinter import *
from tkinter import ttk
import mainApp
import routes
import os
import distanceCalculator
import re
import webbrowser

myFont = 'Helvetica 18 bold'

routeNumber = "73"

def __main__():
    #timetable config info
    tableHeight = 400
    tableWidth = 300
    tableX = 0.5
    tableY = 0.52
    #0.52 to account for the headingof width 2, anchor N (means it takes rel 0.02 off the top)

    #cannot use below functions from configurePage.py - causes circular input
    def configHeader(pageName, headerText):
        headerLabel = tkinter.Label(pageName, text=headerText, font=myFont, width=150, height=2).place(relx=0.5, rely=0, anchor=N)
        homeButton=tkinter.Button(pageName, text="HOME", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[mainApp.__main__(), pageName.destroy()]).place(relx=0.85, rely=0.025, anchor=CENTER)
        routesButton=tkinter.Button(pageName, text="ROUTES", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[routes.routesPage(), pageName.destroy()]).place(relx=0.75, rely=0.025, anchor=CENTER)
    
    def configurePage(pageName):
        pageName.title("Brighter Futures Bus Application")
        pageName.config(bg="#8D16D8")
        pageName.geometry("1920x1080")
    
    #importing tables.py would cause circular import - added modified function here instead
    def generateTimetable(pageName, tableX, tableY, tableHeight, tableWidth):
        #configuring style for table contents
        tableContentsStyle = ttk.Style()
        tableContentsStyle.configure("myStyle.Treeview", font='Helvetica 15')

        #configuring style for headings on tables
        tableStyle = ttk.Style()
        tableStyle.configure("Treeview.Heading", font='Helvetica 18 bold')

        tableContentsFileName = routeNumber
        tableDataFileName = routeNumber
        tableContentsFileName = re.findall(r'\d+', tableContentsFileName)
        tableContentsFileName = (tableContentsFileName[0]+'.txt')
        pathName = (os.getcwd()+'/timetableFiles/txtFiles')
        completeFileName = os.path.join(pathName, tableContentsFileName)
        tableFile = open(completeFileName, 'r')
        tableInput = tableFile.readlines()

        tableDataFileName = re.findall(r'\d+', tableDataFileName)
        tableDataFileName = tableDataFileName[0]+'Data.txt'
        tableDataFile=(os.path.join(pathName, tableDataFileName))
        tableData = open(tableDataFile, 'r')
        tableDataContents = tableData.readlines()

        '''
        print(tableData.readlines())
        ^^testing file output
        '''

        tableFrame = Frame(pageName)
        tableFrame.config(height=tableHeight, width=tableWidth)
        tableFrame.place(relx=tableX, rely=tableY, anchor=CENTER)

        columns = []
        for i in range (1, int(tableDataContents[1])+1):
            columns.append(str(i))

        timetable = ttk.Treeview(tableFrame, style="myStyle.Treeview", height=30)
        timetable['columns']=columns

        timetable.column("#0", width=0, stretch=NO)
        timetable.column("1", width=200, anchor=CENTER)
        for i in range (2, int(tableDataContents[1])+1):
            timetable.column(str(i), width = 100, anchor=CENTER)

        timetable.heading("#0", text="")
        timetable.heading("#1", text="Stop location")
        for i in range (2, int(tableDataContents[1])+1):
            timetable.heading("#"+str(i), text=routeNumber)

        i=0
        c=0
        fileLength = tableDataContents

        #while loop in that inputs timetable data to the table
        while i < int(re.findall(r'\d+', fileLength[2])[0]):
            b=0
            
            tableDataList = []

            '''
            #prints the first row - 0 issues
            if i == 0:
                for b in range(i, int(re.findall(r'\d+', tableDataContents[1])[0])+i):
                    if b < int(re.findall(r'\d+', fileLength[2])[0]):
                        tableDataList.append(tableInput[b])
                        print(tableDataList)
            # prints the second row (some issues so far)
            else:
                for b in range(i, int(re.findall(r'\d+', tableDataContents[1])[0])+i):
                    if b < int(re.findall(r'\d+', fileLength[2])[0]):
                        c+=1
                        for d in range (0, int(re.findall(r'\d+', tableDataContents[1])[0])):
                            tableDataList.append(tableInput[d+c])
                        print(tableDataList)
            # code that didnt really work - just kept repeating the same line again and again
            '''
            while b < int(re.findall(r'\d+', tableDataContents[1])[0]):
                if i==0:
                    tableDataList.append(tableInput[b+i])
                elif b+i+int(re.findall(r'\d+', tableDataContents[1])[0]) <int(re.findall(r'\d+', tableDataContents[2])[0]):
                    tableDataList.append(tableInput[c+int(re.findall(r'\d+', tableDataContents[1])[0])])
                    c+=1
                print(tableDataList)
                b+=1
            
            #writes data to the file
            timetable.insert(parent='', index='end', iid=i, text="", values=tableDataList)

            print(i)
            print(re.findall(r'\d+', tableDataContents[1]))
            i = i+int(re.findall(r'\d+', tableDataContents[1])[0])+1
        '''
        timetable.insert(parent='', index='end', iid=0, text="", values=("Doncaster Interchange", "1000"))
        timetable.insert(parent='', index='end', iid=1, text="", values=("Lakeside Village", "1000"))
        '''

        def OnDoubleClick(self):
            global routeNumber
            selectedItem = timetable.focus()
            selectedStop = timetable.item(selectedItem, "values")[0]
            distanceCalculator.coordGet(selectedStop+" Doncaster")
            distanceCalculator.routing()
            fileName = 'file:///'+os.getcwd()+'/'+'map.html'
            webbrowser.open_new_tab(fileName)

        timetable.bind("<Double-1>", OnDoubleClick)

        tableData.close()
        tableFile.close()
        timetable.pack()

    routePage = tkinter.Tk()

    ##\n needed as route data brings text files new line declaration, meaning text will be uncentered
    configHeader(routePage,'\n'+ "ROUTE "+str(routeNumber))
    configurePage(routePage)
    generateTimetable(routePage, tableX, tableY, tableWidth, tableHeight)
    
    routePage.mainloop()
