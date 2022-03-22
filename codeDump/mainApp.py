import tkinter
from tkinter import *
import tkinter.font as font
import mapGenerationCode
import tables

def main():
    #creates an empty deafault tkinter screen
    mainScreen = tkinter.Tk()

    def loginFunc():
        #login screen tkinter screen
        loginScreen = tkinter.Tk()

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
        headerLabel = tkinter.Label(text="Header Test")
        headerLabel.config(font=(myFont, 20, font.BOLD),width=150, height=2)
        headerLabel.place(relx=0.5, rely=0, anchor=N)


    #calls functions to configure the main page layout
    func = configMain()
    func = configHeader()

    #calls both necessary functions to place the map onto the main screen
    mapGenerationCode.mapSettings(400, 600, "doncaster")
    mapGenerationCode.generate()

    #calls functions to generate the correct table
    tables.tableSettings(700, 750, 0.65, 0.53)
    tables.generateTable()