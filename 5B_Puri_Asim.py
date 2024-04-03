import tkinter as tk 
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter import ttk
from tkinter.ttk import *
from ctypes import windll

#Name: Asim Puri
#Project 5B: GPA Calculation GUI
#============================================
intMsg = "Hours Attempted and Quality points Earned have to be integers."
def __init__(self):
    #self.root = root #Add this eveytime this is used self.root = tkinter.tk() 
    self.root = tk.tk() 
    self.img = tk.PhotoImage(file = "ComputerConsultingGroup.png")
    self.root.iconphoto(True, img)

    self.image_label = tk.Label(self, image = img, text = "Computer Consulting Group",
                                compound= tk.LEFT, font = ("Helvetica", 30, "Bold"))
    self.image_label.grid(row=1, column=1)

    self.tkinter.mainloop()

def calcGPA_clicked():
    #
    points_str = txtPoints.get()
    hours_str = txtHourAttemp.get()
    
    try:
        points = int(points_str)
        hours = int(hours_str)
        isInt = True
    except:
        isInt = False
        global intMsg
        lblIntMsg = ttk.Label(root, borderwidth = 3, text = intMsg, font = ("Helvetica", 10) )
        lblIntMsg.grid(row = 10, column= 1, rowspan= 2, pady= 2)
        clear_clicked()

    if isInt == True:
        gpa = (float(points)/float(hours))
        gpa_text = str(gpa)
        lblMsg = tk.Label(root, bd = 3, text = gpa_text, font = ("Helvetica", 10))
        lblMsg.grid(row=7, column= 3, columnspan=3, rowspan= 2, pady= 2, sticky='e')
        

def continueClick_clicked():
    global msgVar
    global lblMsg
    msgVar = "Continue?"
    lblMsg = tk.Label(root, bd = 3, text = msgVar, font = ("Helvetica", 10))
    lblMsg.grid(row = 18, column =2, columnspan= 3, rowspan= 2, pady= 2, sticky= 'e')

def clear_clicked():
    global txtStudID
    global txtStudName
    global txtCurrCode
    global gpa_text

    txtStudID.delete(0, END)
    txtStudID.insert(0, "")
    txtStudID.grid(row= 2, column = 3, sticky = 'e', pady = 2)
    txtStudID.focus_set()


    txtStudName.delete(0, END)
    txtStudName.insert(0, "")
    txtStudName.grid(row= 3, column = 3, sticky = 'e', pady = 2)

    currCodeVar = StringVar(root)
    currCodeVar.set("T0250")
    lstCurrCode = OptionMenu(root, currCodeVar, "T0250", "PE8596", "GENED8574", "CCNA")
    lstCurrCode.grid(row = 4, column=3, sticky='e', pady=2)

    txtHourAttemp.delete(0, END)
    txtHourAttemp.insert(0,"")
    txtHourAttemp.grid(row= 5, column = 3, sticky = 'e', pady=2)

    txtPoints.delete(0, END)
    txtPoints.insert(0,"")
    txtPoints.grid(row = 6, column = 3, sticky = 'e', pady = 2)
    continueClick_clicked()
    gpa_text = ""

    lblMsg = tk.Label(root, bd = 3, text = " ", width = 15, font = ("Helvetica", 10))
    lblMsg.grid(row= 7, column = 3, columnspan = 3, rowspan = 2, pady = 2, sticky = 'e')


#=============================================
root = tk.Tk()
photo = PhotoImage(file="ComputerConsultingGroup.png")
root.iconphoto(True, photo)
root.geometry('700x400')
root.resizable(True,True)
global gpa_text
gpa_text = ""

root.title("GPA Calculator")
img = tk.PhotoImage(file ="ComputerConsultingGroup.png")
image_label = ttk.Label(root, image = img, text='Student GPA Calculator', compound= tk.LEFT, 
                        font = ("Helvetica", 20))
image_label.grid(row = 1, column =1, sticky = 'w', pady= 2)

lblStudID = ttk.Label(root, text = "StudentID:", font = ("Helvetica", 12))
lblStudID.grid(row = 2, column = 1, sticky = 'e', pady= 2)
txtStudID = ttk.Entry(root)
txtStudID.grid(row = 2, column = 3, sticky = 'e', pady = 2)

lblStudName = ttk.Label(root, text = "Student Name:", font = ("Helvetica", 12))
lblStudName.grid(row= 3, column = 1, sticky = 'e', pady = 2)
txtStudName = ttk.Entry(root)
txtStudName.grid(row = 3, column = 3, sticky = 'e', pady = 2)

lblCurrCode = ttk.Label(root, text = "Curriculum Code:", font = ("Helvetica", 12))
lblCurrCode.grid(row = 4, column= 1, sticky= 'e', pady= 2)
currCodeVar = StringVar(root)
currCodeVar.set("T0250")
lstCurrCode = OptionMenu(root, currCodeVar, "T0250", "PE8596", "GENED8574", "CCNA")
lstCurrCode.grid(row = 4, column = 3, sticky = 'e', pady = 2)

lblHourAttemp = ttk.Label(root, text = "Hours Attempted:", font = ("Helvetica", 12))
lblHourAttemp.grid(row= 5, column= 1, sticky= 'e', pady= 2)
txtHourAttemp = ttk.Entry(root)
txtHourAttemp.grid(row = 5, column = 3, sticky = 'e', pady = 2)

lblPoints = ttk.Label(root, text = "Quality Points Earned:", font = ("Helvetica", 12))
lblPoints.grid(row = 6, column = 1, sticky = 'e', pady = 2)
txtPoints = ttk.Entry(root)
txtPoints.grid(row = 6, column = 3, sticky = 'e', pady = 2)

lblGPA = ttk.Label(root, text = "GPA:", font = ("Helvetica", 12))
lblGPA.grid(row = 7, column = 1, sticky= 'e', pady = 2)
gpa_text = " "

lblMsg = ttk.Label(root, borderwidth = 3, text = gpa_text, font = ("Helvetica", 10))
lblMsg.grid(row = 7, column = 3, columnspan= 3, rowspan= 2, pady = 2, sticky = 'e')



calcButton = Button(root, text = "Calculate\n GPA", command = calcGPA_clicked)
calcButton.grid(row = 9, column = 1, sticky= 'e')

clearButton = Button(root, text= "Clear", command= clear_clicked)
clearButton.grid(row= 9, column= 4)

root.mainloop()