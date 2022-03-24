import tkinter
from tkinter import *
from tkinter import ttk

myFont = 'Helvetica 18 bold'

routeNumber = ""

def __main__():
    #cannot use below functions from configurePage.py - causes circular input
    def configHeader(pageName, headerText):
        headerLabel = tkinter.Label(pageName, text=headerText, font=myFont, width=150, height=2).place(relx=0.5, rely=0, anchor=N)

    def configurePage(pageName):
        pageName.title("Brighter Futures Bus Application")
        pageName.config(bg="#8D16D8")
        pageName.geometry("1920x1080")

    routePage = tkinter.Tk()

    ##\n needed as route data brings text files new line declaration, meaning text will be uncentered
    configHeader(routePage,'\n'+ "ROUTE "+str(routeNumber))
    configurePage(routePage)

    routePage.mainloop()