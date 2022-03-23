import tkinter
from tkinter import *
import tkinter.font as font
from turtle import distance
import webbrowser
import mapGenerationCode
import tables
import os
import distanceCalculator

def mainFunc():
    #creates an empty deafault tkinter screen
    mainScreen = tkinter.Tk()

    #empty template variables
    myFont=""

    #configures size of screen, font on the screen, the screen title, and background colour
    def configMain():
        global myFont
        myFont = font.Font(family = 'american typewriter') #creates a font variable to be used
        mainScreen.geometry("1920x1080") #window size
        mainScreen.title("Brighter Futures Bus application") #window title
        mainScreen.config(bg="#8D16D8")

    #configuers the screens header and places it
    def configHeader():
        global myFont
        headerLabel = tkinter.Label(text="Home Screen")
        headerLabel.config(font=(myFont, 20, font.BOLD),width=150, height=2)
        headerLabel.place(relx=0.5, rely=0, anchor=N)

    def configMap():
        distanceCalculator.coordGet("Bawtry Road")
        distanceCalculator.routing()
        fileName = 'file:///'+os.getcwd()+'/'+'map.html'
        webbrowser.open_new_tab(fileName)

    #calls functions to configure the main page layout
    configMain()
    configHeader()

    #calls both necessary functions to place the map onto the main screen
    mapGenerationCode.mapSettings(400, 600, "doncaster")
    mapGenerationCode.generate()

    #calls functions to generate the correct table
    tables.tableSettings(700, 750, 0.65, 0.53)
    tables.generateTable()
    
    #test button
    test = tkinter.Button(text="test", command=configMap)
    test.place(relx=0.5, rely=0.75)