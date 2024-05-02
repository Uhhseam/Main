##--------------------------------------------------------------
## Project: Class Room Size
## Name: Asim Puri
## Date: 02/12/2024
##--------------------------------------------------------------

class Room():
    
    counter = 0
        
    def __init__(self):
        self.length = self.checkDigit("length")
        self.width = self.checkDigit("width")
        area = self.calcArea()
        perimiter = self.calcPerimeter()
        self.printStr(area,perimiter)
        Room.counter +=1
        

    def checkDigit(self, msg):
        number = float(input("Please Enter a number for " + msg + ":" + "\n>>> "))
        print(str(number) + " is number  <-----------------" +"for " + msg)
        return number

    def calcArea(self):
        print (str(self.length) + " length <------> width " + str(self.width))
        return(self.length * self.width)

    def calcPerimeter(self):
        '''#####  You must create this method to calculate the perimeter.
                  Assume that you calculate perimeter by adding  all the sides'''
        return(self.length + self.width)
        

    def printStr(self, pArea, perimiter):
        print ("Length of: " + str(self.length)+ "\n" +
                "Width of: " + str(self.width) + "\n" +
                "Area is **: " + str(pArea) + "\n" +
                "Perimeter is: " +str(perimiter))
        
def main():
    again = True
    newRoom = Room()
    while again == True:
        another = input("Enter another roomSize y/n ? ")
        if another.lower() == "n":
            again = False
        else: newRoom = Room()
    print("Total rooms evaluated: " + str(Room.counter))
    
'''========================================================================'''
main()
