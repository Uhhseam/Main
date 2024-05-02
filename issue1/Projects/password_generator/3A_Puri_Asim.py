studId = str(7)
pastPasswords = [[10],[3]]
specialCharacters = ["!","@","#","$","%","^","&","*","(",")",
                     "-","_","{","}","[","]",";",":","<",">","?","/","~","|"]
class passwordGenerator():
    studCount = int(0)

    def __init__(self):
        passWord = self.getPassWord()
        self.checkPassWord(passWord)
        studId = str(7)

    def getPassWord(self):
        passWord = input("Please Enter a password that has: \n"+
                         " 1) a capital letter\n" +
                         " 2) Special Character (!@#$%^&*())\n" +
                         " 3) a Number\n"+
                         " 4) Length of at lease 5 characters\n" +
                         "--> ")
        return passWord
    
    def checkPassWord(self, pswd):
        upCase = 0
        num = 0
        specialChar = 0
        lengthOfPswd = 0

        if len(pswd) >= 5:
            for char in pswd:
                if (char.isupper() == True):
                    upCase = 1
                elif (char.isdigit()):
                    num = True
                elif char in specialCharacters:
                    specialChar = True

        if (upCase == True & num == True & specialChar == True):
            print("Yeah! Your password meets security criteria")
        else:
            if not(len(pswd) >= 5):
                print("Your passowrd length is " + str(len(pswd)))
            if(not upCase):
                print("\nYou must enter an uppercase character")
            if (bool(num) == False):
                print("\nYou must enter a numeric character")
            if(bool(specialChar) == False):
                print("\nYou must enter a special character")
            print("\nPlease try again")


def main():
    again = True
    while again == True:
        newPassWord = passwordGenerator()
        again = input("\nEnter another password y/n? ")
        if again.lower() == "n":
            again = False
        elif again.lower() == "y":
            again = True

main()
                
