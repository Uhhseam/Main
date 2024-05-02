import tkinter as tk #1
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter.ttk import *

from ctypes import windll

def continueClick_clicked():
    print("Continue?")
    
def clear_clicked():
    ePrincipalAmt.delete(0,END)
    ePrincipalAmt.focus_set()
    eIntRate.delete(0,END)
    einTerm.delete(0,END)
    ePayment.delete('1.0',tk.END)
    #ePayment.set("")

def calcPayment_clicked():

    try:
        rte = float(inIntRate.get())
        lAmt = float(inPrincipleAmt.get())
        term = int(inTerm.get())
        payment = (rte/12) * (1/(1-(1+rte/12)**(-term)))*lAmt

        totalPd = payment * term
        intrestAmt = totalPd - lAmt
        payStr = "Payment is " + "${:,.2f}".format(payment) + ".\nYou will pay " + \
            "${:,.2f}".format(totalPd) + " over the life of the loan.\nIntrest Paid " + \
            "${:,.2f}".format(totalPd - lAmt)
        ePayment.insert(tk.END, payStr)
        ePayment.grid(row = 6, rowspan = 4, column = 2, columnspan = 3, sticky = W, pady = 2)
    except ValueError:
        ePayment.delete(0,tk.END)
        #ePayment
        ePayment.grid(row = 6, rowspan = 4, column = 2, columnspan = 3, sticky = W, pady = 2)


#================
root = tk.Tk()
photo = PhotoImage(file=r"ComputerConsultingGroup.png")
root.iconphoto(True, photo)
root.geometry('800x700')
root.resizable(True,True)
root.title("Determine Payment")
img = tk.PhotoImage(file = r"ComputerConsultingGroup.png")
image_label = tk.Label(root, image = img, text='GUI Payment Calculator', compound = tk.LEFT)
image_label.grid(row = 1, column = 1, sticky = W, pady = 2)

lblPrincipalAmt = ttk.Label(root, text = "Amount of Loan: ", font = ("Helvetica", 12))
lblPrincipalAmt.grid(row = 2, column = 1, sticky = E, pady = 2)
inPrincipleAmt = StringVar()
ePrincipalAmt = ttk.Entry(root, textvariable = inPrincipleAmt, width = 15)
ePrincipalAmt.grid(row = 2, column = 2, sticky = W, pady = 2)
ePrincipalAmt.focus_set()

lblIntRate = ttk.Label(root, text = "Intrest rate of loan in percentAPR: ", font = ("Helvetica", 10))
strIntRate = StringVar()
lblIntRate.grid(row = 3, column = 1, sticky = E, pady = 2)
inIntRate = StringVar()
eIntRate = ttk.Entry(root, textvariable = inIntRate, width = 15)
eIntRate.grid(row = 3, column = 2, sticky = W, pady = 2)

lblTerm = ttk.Label(root, text = "Term of loan in months: ", font = ("Helvetica", 10))
strTerm = str()
lblTerm.grid(row = 4, column = 1, sticky = E, pady = 2)
inTerm = StringVar()
einTerm = ttk.Entry(root, textvariable = inTerm, width = 15)
einTerm.grid(row = 4, column = 2, sticky = W, pady = 2)


calcButton = Button(root, text = "Calculate Payment", command = calcPayment_clicked)
calcButton.grid(row = 5, column = 2)

clearButton = Button(root, text = "Clear", command = clear_clicked)
clearButton.grid(row = 5, column = 3)

lblPmtMsg = tk.Label(root, text = "Payment: ", font = ("Helvetica", 10))
lblPmtMsg.grid(row = 6, column = 1, sticky = E, pady = 2)
payStr = StringVar()
PayStr = "Hello"
ePayment = tk.Text(root, width=35, height = 4)
ePayment.grid(row = 6, rowspan = 3, column = 2, columnspan = 2, pady = 2)


root.after(200000, continueClick_clicked)
root.mainloop()