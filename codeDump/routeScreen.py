import tkinter
from tkinter import *
from tkinter import ttk
import mainApp
import routes

myFont = 'Helvetica 18 bold'

routeNumber = ""

def __main__():
    #cannot use below functions from configurePage.py - causes circular input
    def configHeader(pageName, headerText):
        headerLabel = tkinter.Label(pageName, text=headerText, font=myFont, width=150, height=2).place(relx=0.5, rely=0, anchor=N)
        homeButton=tkinter.Button(pageName, text="HOME", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[mainApp.__main__(), pageName.destroy()]).place(relx=0.85, rely=0.025, anchor=CENTER)
        routesButton=tkinter.Button(pageName, text="ROUTES", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[routes.routesPage(), pageName.destroy()]).place(relx=0.75, rely=0.025, anchor=CENTER)
    def configurePage(pageName):
        pageName.title("Brighter Futures Bus Application")
        pageName.config(bg="#8D16D8")
        pageName.geometry("1920x1080")

    routePage = tkinter.Tk()

    ##\n needed as route data brings text files new line declaration, meaning text will be uncentered
    configHeader(routePage,'\n'+ "ROUTE "+str(routeNumber))
    configurePage(routePage)

    routePage.mainloop()