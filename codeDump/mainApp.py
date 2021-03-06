import tkinter
from tkinter import *
import tkinter.font as font
import webbrowser
import mapGenerationCode
import configurePage
import tables
import os
import distanceCalculator
import routeScreen
import time

myFont='Helvetica 18 bold'

admin = False

def __main__():
    global admin
    #creates an empty deafault tkinter screen
    mainScreen = tkinter.Tk()

    def configMap():
        distanceCalculator.coordGet("Bawtry Road")
        distanceCalculator.routing()
        fileName = 'file:///'+os.getcwd()+'/'+'map.html'
        webbrowser.open_new_tab(fileName)

    #calls functions to configure the main page layout
    configurePage.configure(mainScreen)
    configurePage.configHeader(mainScreen, "Main Screen")

    #creates a border for the map
    borderLabel = tkinter.Label(mainScreen, bg = "yellow", width=45, height=40).place(relx=0.2, rely=0.55, anchor=CENTER)

    #calls both necessary functions to place the map onto the main screen
    mapGenerationCode.mapSettings(400, 600, "doncaster")
    mapGenerationCode.generate(mainScreen)

    #code to refresh the map
    def resetMap():
        #calls both necessary functions to place the map onto the main screen
        mapGenerationCode.mapSettings(400, 600, "doncaster")
        mapGenerationCode.generate(mainScreen)
    
    mapButton = tkinter.Button(mainScreen, font=myFont, text="RESET POSITION", command=lambda:[resetMap()])
    mapButton.place(relx=0.2, rely=0.9, anchor=N)

    #calls functions to generate the correct table
    tables.tableSettings(700, 750, 0.65, 0.53)
    tables.generateTable(mainScreen)
    
    '''
    testButton = tkinter.Button(text="test", command=routeScreen.__main__).place(relx=0.5, rely=0.5)
    ^ test button to test connection to route screen, and changing of displayed information
    '''

    if admin == True:
        configurePage.configSettingsButton(mainScreen)
    '''
    #test button
    test = tkinter.Button(text="test", command=configMap)
    test.place(relx=0.5, rely=0.05, anchor=CENTER)
    '''
    mainScreen.mainloop()