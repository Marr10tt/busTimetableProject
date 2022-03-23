import tkinter
from tkinter import *
import tkinter.font as font
import webbrowser
import mapGenerationCode
import configurePage
import tables
import os
import distanceCalculator

myFont='Helvetica 18 bold'

admin = False

def mainFunc():
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

    '''
    #calls both necessary functions to place the map onto the main screen
    mapGenerationCode.mapSettings(400, 600, "doncaster")
    mapGenerationCode.generate()
    '''
    #calls functions to generate the correct table
    tables.tableSettings(700, 750, 0.65, 0.53)
    tables.generateTable(mainScreen, mainScreen)
    
    if admin == True:
        configurePage.configSettingsButton(mainScreen)
    '''
    #test button
    test = tkinter.Button(text="test", command=configMap)
    test.place(relx=0.5, rely=0.05, anchor=CENTER)
    '''