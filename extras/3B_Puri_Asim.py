import os
import time
#
#
#
#
#
class Customer():

    C_TotalCurrentBalance = 0.0


    def __init__(self):

        cusName = str(15)
        cusNumber = int(6)
        cusAvlCredit = float(5)
        cusLimit = float(5)
        cusCurrentBalance = float(5)
        start = time.time()
        self.displayInstructions()
        print("*** In init ***")

        self.cusName = self.validString("Customer Name: ")
        self.cusNumber = self.validNumber("Account Number: ")
        self.cusCurrentBalance = float(self.validFloat("Customer Balance: "))
        self.cusLimit = float(self.validFloat("Credit Limit: "))
        self.cusAvlCredit = self.CalcAvlCredit()
        self.writeToFile()
        print(f'Time Elapsed: {time.time() - start}')


    def displayInstructions(self):
        """Display customer instrucitons"""
        print("You will be creating a customer data file")


    def askYesNo(self,question):
        """Asks a yes or no question"""
        response = None
        while response not in ("y", "n", "Y", "N"):
            response = input(question).lower()
        return response
    
    def CalcAvlCredit(self):
        """Calculates and returns the balance owed"""
        avlCredit = (self.cusLimit - self.cusCurrentBalance)
        Customer.C_TotalCurrentBalance += avlCredit
        return (avlCredit)
    
    def writeToFile(self):
        print("\n\n*** writeToFile ***")
        try:
            outFile = open("customer.txt","a")
            outFile.write(self.printStr())
            outFile.close()
        except:
            print("Unable to write to file: ")

    def printStr(self):
        print("*** printStr")

        fName = input("Enter filename and extension: ")

        try:
            with open(fName,'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row + "\n")
        except IOError:
            print("Can't find the file" + fName + ". Please check file Name: ")

        return(str(self.cusNumber + "," + self.cusName + "," + str(self.Balance) + "," +
                   str(self.cusLimit) + "," + str(self.cusCurrentBalance)) + "\n")
    
    def validString(self, whoTest):
        goodData = False
        goodString = input("Enter " + whoTest + " : ")
        while not goodData:
            if(len(goodString) <= 0):
                goodString = input("\nInvalid" + whoTest + ". Enter customer Name: ")
            else:
                goodData = True
        return goodString
    
    def validNumber(self, numTest):
        goodData = False
        goodNum = input("Enter " + numTest + " : ")
        while not goodData:
            if (goodNum.isdigit()):
                goodData = True
            else:
                goodNum = input("\nInvalid "+ numTest + ". Enter valid " + numTest + ": ")
        return goodNum
    
    def validFloat(self, fltMsg):
        goodData = False
        goodNum = input("Enter " + fltMsg + " : ")
        while not goodData:
            try:
                if(float(goodNum)):
                    goodData = True
            except ValueError:
                goodNum = input("\nInvalid " + fltMsg + ". Enter valid " + fltMsg + ": ")
        return goodNum
    

def readFromFile():
    print("*** readFromFile")
    inFile = open("customer.txt","r")
    print("\n\n\nOpened student.txt")
    nlines = inFile.readlines()
    print(nlines)
    inFile.close()
#================
    
def main():
    answer = "y"
    while not answer.lower() == "n":

        anotherCustomer = Customer()
        answer = anotherCustomer.askYesNo("Would you like to enter another customer? y/n ")

    readFromFile()



main()