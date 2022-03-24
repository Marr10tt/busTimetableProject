import tkinter
from tkinter import *
import tkinter.font
import hashlib
import mainApp
import configurePage
import tkmacosx
#^^tkmacosx is unused - buttons do not work as expected

loginScreen = Tk()

#dictionary to store the hashed usernames and passwords
userPassDict = {
    "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":"5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5",
    "264c8c381bf16c982a4e59b0dd4c6f7808c51a05f64c35db42cc78a2a72875bb":"264c8c381bf16c982a4e59b0dd4c6f7808c51a05f64c35db42cc78a2a72875bb"
}

#variables for login validation
loginTries = 3
invalidMessageText = ("invalid username or password, you have", loginTries, "attempts remaining")
invalidMessage = tkinter.Label(text=invalidMessageText, bg='#8D16D8', font='Helvetica 18 bold', fg="red")

#all code to validate user input - including hashing values
def inputVal():
    #imports necessary variables
    global userPassDict
    global loginTries
    global invalidMessageText

    #gets user input and stores as variables
    #converts username input to hashed value
    username=hashlib.sha256((userBox.get()).encode()).hexdigest()

    #converts password input to hashed value
    password=hashlib.sha256((passBox.get()).encode()).hexdigest()

    #checks for the username in the dictionary
    if username in userPassDict:
        if userPassDict[username] == password:
            if username=="8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
                mainApp.admin=True
                print("Admin enabled")

            loginScreen.destroy()
            mainApp.__main__()
        else:
            #removes 1 try, displays appropriate message
            loginTries-=1
            invalidMessageText=("invalid username or password, you have", loginTries, "attempts remaining")
            invalidMessage = tkinter.Label(text=invalidMessageText, bg='#8D16D8', font='Helvetica 18 bold', fg="red")
            invalidMessage.place(relx=0.5, rely=0.35, anchor=CENTER)
            #if there are no tries remaining, the application closes
            if loginTries <=0:
                loginScreen.quit()
    else:
        #removes 1 try, displays appropriate message
        loginTries-=1
        invalidMessageText=("invalid username or password, you have", str(loginTries), "attempts remaining")
        #refreshes and replaces invalid message
        invalidMessage = tkinter.Label(text=invalidMessageText, bg='#8D16D8', font='Helvetica 18 bold', fg="red")
        invalidMessage.place(relx=0.5, rely=0.35, anchor=CENTER)
        if loginTries <=0:
            #if there are no tries remaining, the application closes
            loginScreen.quit()

#configures text boxes and their headings
userLabel = tkinter.Label(text="USERNAME", bg="#8D16D8", font='Helvetica 18 bold')
passLabel = tkinter.Label(text="PASSWORD", bg="#8D16D8", font='Helvetica 18 bold')
userBox = tkinter.Entry()
passBox = tkinter.Entry(show="*")

#places text boxes and their headings
userLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
userBox.place(relx=0.5, rely=0.4, anchor=CENTER)
passLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
passBox.place(relx=0.5, rely=0.6, anchor=CENTER)

#LOGIN button
loginButton = tkinter.Button(text="LOGIN", background="yellow", activebackground="#9b870c", font='Helvetica 18 bold', command=inputVal)
loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

'''
loginButton = Button(text="LOGIN", background="yellow", activebackground="#9b870c", font='Helvetica 18 bold', command=inputVal)
loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)
'''

configurePage.configure(loginScreen)
loginScreen.geometry("250x400+560+220")
#^^places in centre of
'''
loginScreen.geometry("250x400")
^^ places in top left, not centre
'''
loginScreen.mainloop()