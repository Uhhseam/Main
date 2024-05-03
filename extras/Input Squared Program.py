import tkinter as tk #1
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter import ttk
from tkinter.ttk import *

from ctypes import windll

global msgStr
global inNum1
global lblinNum
global eNumSquared
global errorMsg
global lblMsg
global msgLbl
global msgVar
#============================
def __init__(self):
    #Create the main window
    self.root = tk.Tk()
    self.img = tk.PhotoImage(file = "ComputerConsultingGroup.png")
    self.root.iconphoto(True, img)

    self.image_label = tk.Label(self, image = img, text = "Computer Consulting Group",
                                compound = tk.LEFT, font = ("Helvetica", 30, "bold"))
    self.image_label.grid(row = 1, column = 1)

    self.tkinter.mainloop()

def continueClick_clicked():
    global msgVar
    global lblMsg
    msgVar = "Continue?"
    lblMsg = tk.Label(root, bd = 3, text = msgVar, font = ("Helvetica", 10))
    lblMsg.grid(row = 18, column = 2, columnspan = 3, rowspan = 2, pady = 2, sticky = W)

def clear_clicked():
    global lblMsg
    global eNumSquared
    global msgStr
    global msgVar
    msgStr = ""
    msgVar = ""
    
    eNumSquared.destroy()
    lblMsg.destroy()
    msgVar = ""

    lblMsg = tk.Label(root, bd = 3, text = "", font = ("Helvetica", 10))
    lblMsg.grid(row = 18, column = 2, columnspan = 3, rowspan = 2, pady = 2, sticky = W)

    lblinNum.focus_set()

def calcSquared_clicked():
    clear_clicked()
    numSquared = 0
    global msgStr
    global inNum1
    global lblinNum
    global eNumSquared
    msgStr = ""
    try:
        inNum1 = float(lblinNum.get())

        if float(inNum1) > 0:
            numSquared = inNum1 * inNum1

            msgStr = StringVar()
            msgStr = ("Number is {:,.1f}".format(inNum1)+".\nThe number squared is "+
                      "{:,.1f}".format(numSquared)+".")
            eNumSquared = Label(root, text = msgStr, font = ('Helvetica 10 bold'))
            eNumSquared.config(state = "disabled")
            eNumSquared.grid(row = 13, rowspan = 3, column = 2, columnspan = 3)

    except ValueError:
        global msgVar
        global lblMsg
        msgVar = "Error in Number; Please try again"
        lblMsg = tk.Label(root, bd =3, text = msgVar, font = ("Helvetica", 10))
        lblMsg.grid(row = 18, column= 2, columnspan= 3, rowspan= 2, pady= 2, sticky= W)

        lblinNum.focus_set()

#=======================================
root = tk.Tk()
photo = PhotoImage(file=r"ComputerConsultingGroup.png")
root.iconphoto(True, photo)
root.geometry('600x300')
root.resizable(True,True)
root.title("Number Squared")
img = tk.PhotoImage(file=r"ComputerConsultingGroup.png")
image_label = ttk.Label(root, image = img, text = 'GUI Input', compound= tk.LEFT,
                        font = ("Helvetica", 22))
image_label.grid(row = 1, column = 1, sticky = W, pady =2)


lblNum1 = ttk.Label(root, text = "Enter a number:", font= ("Helvetica", 12))
lblNum1.grid(row = 2, column = 1, sticky = E, pady = 2)

inNum1 = StringVar()
lblinNum = ttk.Entry(root, textvariable= inNum1, justify = LEFT, width = 20)
lblinNum.grid(row =2, column =2, columnspan = 2, sticky = E, pady = 2)


calcButton = Button(root, text = "Calculate\n Squared", command = calcSquared_clicked)
calcButton.grid(row = 6, column = 2)

clearButton = Button(root, text = "Clear\n", command = clear_clicked)
clearButton.grid(row = 6, column = 3)

msgStr = StringVar()
msgStr = "\n\n"
eNumSquared = Label(root, text = msgStr, font= ('Helvetica 10 bold'))
eNumSquared.config(state = "enabled")
eNumSquared.grid(row = 13, rowspan= 3, column = 2, columnspan= 3)

msgVar = StringVar()
msgVar = "\n\n"
lblMsg = tk.Label(root, bd = 3, text = msgVar, font = ("Helvetica", 10))
lblMsg.grid(row = 18, column= 2, columnspan= 3, rowspan= 2, pady = 2, sticky= W)


root.after(5000, continueClick_clicked)
root.mainloop()