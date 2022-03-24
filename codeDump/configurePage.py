import tkinter
from tkinter import *
from tkinter import font
import routes
import mainApp
import webScraper

myFont = "Helvetica 18 bold"

#configures the base settings for every page on the app
def configure(pageName):
    pageName.config(bg='#8D16D8')
    pageName.title("Brighter Futures Bus Application")
    pageName.geometry("1920x1080")

#configuers the screens header and places it
def configHeader(pageName, pageTitle):
    global myFont
    headerLabel = tkinter.Label(pageName, text=pageTitle)
    headerLabel.config(font=myFont,width=150, height=2)
    headerLabel.place(relx=0.5, rely=0, anchor=N)
    homeButton=tkinter.Button(pageName, text="HOME", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[mainApp.__main__(), pageName.destroy()])
    homeButton.place(relx=0.85, rely=0.025, anchor=CENTER)
    routesButton=tkinter.Button(pageName, text="ROUTES", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[routes.routesPage(), pageName.destroy()])
    routesButton.place(relx=0.75, rely=0.025, anchor=CENTER)

def configSettingsButton(pageName):
    settingsButton = tkinter.Button(pageName, text="SETTINGS", background="yellow", activebackground="#9b870c", font=myFont, command=lambda:[settingsTopLevel()])
    settingsButton.place(relx=0.95, rely=0.025, anchor=CENTER)

def settingsTopLevel():
    settingsPage = tkinter.Toplevel()
    settingsPage.title("Brighter Futures Bus Application")
    settingsPage.config(bg='#8D16D8')
    settingsPage.geometry("960x540+250+150")
    headerLabel = tkinter.Label(settingsPage, text="SETTINGS")
    headerLabel.config(font=myFont,width=150, height=2)
    headerLabel.place(relx=0.5, rely=0, anchor=N)
    settings(settingsPage)

def settings(pageName):
    logoutButton = tkinter.Button(pageName, font=myFont, text="LOGOUT", command=lambda:[logout(pageName)])
    logoutButton.place(relx=0.5, rely=0.5, anchor=CENTER)
    newRouteButton = tkinter.Button(pageName, font=myFont, text="NEW ROUTE", command=lambda:[newRoute()])
    newRouteButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def logout(pageName):
    pageName.quit()

def newRoute():
    routeList = open("routeList.txt", "a")

    newRouteInfo = {
        "Number":"",
        "Name":"",
        "URL":""
    }
    #config page
    newRoutePage = tkinter.Toplevel()
    newRoutePage.title("Brighter Futures Bus Application")
    newRoutePage.config(bg='#8D16D8')
    newRoutePage.geometry("960x540+250+150")
    #^^ places in direct center of page
    
    #config header
    headerLabel = tkinter.Label(newRoutePage, text="NEW ROUTE")
    headerLabel.config(font=myFont,width=150, height=2)
    headerLabel.place(relx=0.5, rely=0, anchor=N)

    #config entry fields
    routeNumber = tkinter.Entry(newRoutePage, font=myFont)
    routeName = tkinter.Entry(newRoutePage, font=myFont)
    routeURL = tkinter.Entry(newRoutePage, font=myFont)

    #place entry fields
    routeNumber.place(relx=0.5, rely=0.4, anchor=CENTER)
    routeName.place(relx=0.5, rely=0.5, anchor=CENTER)
    routeURL.place(relx=0.5, rely=0.6, anchor=CENTER)

    #config entry labels
    tkinter.Label(newRoutePage, font=myFont, text="route number", bg='#8D16D8').place(relx=0.2, rely=0.4, anchor=W)
    tkinter.Label(newRoutePage, font=myFont, text="route name", bg='#8D16D8').place(relx=0.2, rely=0.5, anchor=W)
    tkinter.Label(newRoutePage, font=myFont, text="route URL", bg='#8D16D8').place(relx=0.2, rely=0.6, anchor=W)

    def scrape():
        #scrapes web using given url and saves in new file with corresponding route number as file title
        webScraper.webScrape(newRouteInfo["URL"], newRouteInfo["Number"])

    def setInformation():
        #validity check
        if routeName.get()!="" and routeNumber.get()!="" and routeURL.get()!="":
            #set dictionary values
            newRouteInfo["Name"]=routeName.get()
            newRouteInfo["Number"]=routeNumber.get()
            newRouteInfo["URL"]=routeURL.get()

            routeList.write('\n')
            routeList.write(newRouteInfo["Number"])
            routeList.write('\n')
            routeList.write(newRouteInfo["Name"])

            print(newRouteInfo["Name"])

            routeList.close()

            scrape()

            newRoutePage.destroy()
        else:
            displayError(newRoutePage, 0.5, 0.3, "1 or more text field(s) are empty, please correct and try again")

    def displayError(pageName, posX, posY, errorMessage):
        errorLabel = tkinter.Label(pageName, bg="#8D16D8", fg="red", font=myFont, text=errorMessage).place(relx=posX, rely=posY, anchor=CENTER)
    #confirmation button
    confirmButton = tkinter.Button(newRoutePage, font=myFont, text="CONFIRM", command = lambda:[setInformation()]).place(relx=0.5, rely=0.7, anchor=CENTER)
