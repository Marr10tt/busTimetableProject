import tkinter
from tkinter import *
import tkinter.font as font
import tkinter.ttk
import mapGenerationCode
import webScraper

#creates an empty deafault tkinter screen
mainScreen = tkinter.Tk()

#empty template variables
myfont=""

#configures size of screen, font on the screen, the screen title, and background colour
def configMain():
    global myfont
    myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
    mainScreen.geometry("1920x1080") #window size
    mainScreen.title("Brighter Futures Bus application") #window title
    mainScreen.config(bg="#8D16D8")

#configuers the screens header and places it
def configHeader():
    headerLabel = tkinter.Label(text="Header Test")
    headerLabel.config(font=(myfont, 20, font.BOLD),width=150, height=2)
    headerLabel.place(relx=0.5, rely=0, anchor=N)

#calls both necessary functions to place the map onto the main screen
mapGenerationCode.mapSettings(400, 600, "doncaster")
mapGenerationCode.generate(mapGenerationCode.windowWidth, mapGenerationCode.windowHeight, mapGenerationCode.Location)

#calls functions to configure the main page layout
func = configMain()
func = configHeader()

mainScreen.mainloop()