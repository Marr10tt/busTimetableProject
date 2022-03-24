import tkinter
from tkinter import *
from tkinter import font
import configurePage
import tables

myFont = "'Helvetica 18 bold'"

def routesPage():
    routePage = tkinter.Tk()
    global myFont

    #calls page configuration functions
    configurePage.configure(routePage)
    configurePage.configHeader(routePage, "Routes")

    '''
    #tests label placement
    testLabel = tkinter.Label(routePage, text="test")
    testLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
    '''
    #generates sample table
    tables.tableSettings(700, 750, 0.5, 0.53)
    tables.generateTable(routePage)