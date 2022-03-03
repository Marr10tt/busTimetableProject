from importlib import import_module
import tkinter
import tkinter.font as font
import tkinter.ttk
import mapGenerationCode
import webScraper

#creates an empty deafault tkinter screen
mainScreen = tkinter.Tk()

def configMain():
    myfont = font.Font(family = 'american typewriter') #creates a font variable to be used
    mainScreen.geometry("1920x1080") #window size
    mainScreen.title("Brighter Futures Bus application") #window title
    mainScreen.config(bg="#8D16D8")

def configHeader():
    headerLabel = tkinter.Label(text="Header Test")
    headerLabel.place(relx=0.5, rely=0)

mapGenerationCode.generate()

#calls functions
func = configMain()
func = configHeader()

mainScreen.mainloop()