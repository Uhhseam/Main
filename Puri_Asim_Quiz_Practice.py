import tkinter as tk #1
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from tkinter.ttk import *
from ctypes import windll #used to get a sharper image on the screen

#==========================================================
#Project to introduce the TOE chart and its use in planning
#Date: 03/07/2024
#Name: Asim Puri
#===========================================================
total2 = 0
grandTotal = 0

def writeToDisk_clicked():
    print("\n\n******  writeToFile  ******")
    cName = CusName.get()
    Name = ProductName.get()
    price = float(inPrice.get())
    qty = int(inQty.get())
    extendedPrice = calcExtendedPrice(price, qty) 
   
    msg_str = (cName + "," + Name + ","  + str(price) + "," + str(qty) + "," + str(extendedPrice) + "\n")
         
    outFile = open("salesFile.csv", "a")
    outFile.write(str(msg_str))
    outFile.close()
       
def dspMore_clicked():
    showinfo(title = 'Continue?', message ="Do you Want to continue?" )

def calcExtendedPrice(price, qty):
    global total2
    price = float(price)
    qty = int(qty)
    total1 = price*qty
    total2 += total1
    return "$" + str(total1),"$" + str(total2)

def clearNext_clicked():
    
    ProductName.delete(0, tk.END)
    PriceIn.delete(0, tk.END)
    QtyIn.delete(0, tk.END)
    
    ProductName.focus_set()

def clearAll_clicked():
    global total2
    dspMore_clicked()
    CusName.delete(0,END)
    ProductName.delete(0, END) #
    PriceIn.delete(0, END) #
    QtyIn.delete(0, END) #
    msgString.delete("1.0", "end")
    CusName.focus_set()
    msgTotal.delete(1.0, tk.END)
    
    msg_str = initMsg()
    msgString.insert(tk.END, msg_str)
    msgString.grid(row = 10, column = 2)
    gt_str = initGtMsg()
    msgTotal.insert(tk.END, gt_str)
    msgTotal.grid(row = 11, column = 2)
    total2 = 0
     

def initMsg():
    msg_str = ("Name\tProduct\tQty\tPrice\tExtended Price\n")
    return msg_str

def initGtMsg():
     gt_str = ("0.0")
     return gt_str

def dspMsg_clicked():
    cName = inCusName.get()
    Name = inProductName.get()
    Qty = inQty.get()
    Price = float(inPrice.get())
    eprice, grandTotal = calcExtendedPrice(Price, Qty)
    msg_str = (cName +"\t" + Name +"\t" + str(Qty) +"\t" + str(Price) +"\t" + eprice + "\n")
    msgString.insert(tk.END, msg_str)
    msgString.grid(row = 10, column = 2)
    
    msgTotal.delete(1.0, tk.END)
    msgTotal.insert(tk.END, grandTotal)
    msgTotal.grid(row= 11, column= 2)
    writeToDisk_btn.focus_set()
       
#====================================================================
#Set up Form
#====================================================================
windll.shcore.SetProcessDpiAwareness(1)  #used to have a sharper text

#set up and add download button
root = tk.Tk() #Creates a window using name of root.  You do not have to have the name root if you don't want to

root.geometry('1300x700') #Sets window size
root.resizable(True,True) #true allows for vertical, horizontal
root.title("Extending a Price") #Title of Window
img = tk.PhotoImage(file = "ComputerConsultingGroup.png")
root.iconphoto(True, img) #sets photo
image_label = tk.Label(root, image = img, text='Computer Consulting Group', compound = tk.LEFT, font = ("Helvetica", 13, "bold")) #Used to set the alignment to left
image_label.grid(row = 1,column = 1)

lblCusName = ttk.Label(root,text="Enter Customer name: ", font = ("Helvetica", 12))
lblCusName.grid(row = 4, column = 1)
inCusName = StringVar()
CusName = ttk.Entry(root, textvariable = inCusName, justify = LEFT, width = 15)
CusName.focus_set()
CusName.grid(row = 4, column = 2)

lblProductName = ttk.Label(root,text="Enter Product name: ", font = ("Helvetica", 12))
lblProductName.grid(row = 5,column = 1)
inProductName = StringVar()
ProductName = ttk.Entry(root, textvariable = inProductName, justify = LEFT, width = 15)
ProductName.grid(row =5, column = 2)

lblQty = ttk.Label(root,text="Enter Qty to purchase: ", font = ("Helvetica", 12))
lblQty.grid(row = 6, column = 1)
inQty = StringVar()
QtyIn = ttk.Entry(root, textvariable = inQty, justify = LEFT, width = 15)
QtyIn.grid(row = 6, column = 2)

lblPrice = ttk.Label(root,text="Enter Price: ", font = ("Helvetica", 12))
lblPrice.grid(row = 7, column = 1)
inPrice = StringVar()
PriceIn = ttk.Entry(root, textvariable = inPrice, justify = LEFT, width = 15)
PriceIn.grid(row = 7 , column = 2)

dspMsg_btn = ttk.Button(root, text = "Calculate extended cost",command=dspMsg_clicked)
dspMsg_btn.grid(row = 5, column = 5)

writeToDisk_btn = ttk.Button(root, text = "Write to Disk",command=writeToDisk_clicked)
writeToDisk_btn.grid(row = 6, column = 5)

clearNext_btn = ttk.Button(root, text = "Input another item?",command=clearNext_clicked)
clearNext_btn.grid(row = 7, column = 5)
clearAll_btn = ttk.Button(root, text = "Input another person?",command=clearAll_clicked)
clearAll_btn.grid(row = 8, column = 5)
# Create an Exit button.
exit_btn = ttk.Button(root, text = "Exit",
            command = root.destroy)
exit_btn.grid(row = 9, column = 5)

msgString = tk.Text(root, height = 4, width = 50, wrap = WORD)
msg_str = initMsg()
msgString.insert(tk.END, msg_str)
msgString.grid(row = 10, column = 2)

lblTotal = ttk.Label(root,text="Grand Total:  ", font = ("Helvetica", 12))
lblTotal.grid(row = 11, column = 1)
msgTotal = tk.Text(root, height = 1, width = 10)
gt_str = initGtMsg()
msgTotal.insert(tk.END, gt_str)
msgTotal.grid(row = 11, column = 2)

root.after(200000, dspMore_clicked)
root.mainloop()

#================================================================================
    

    
