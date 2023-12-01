##--------------------------------------------------------------
## 8A Process dictionary information 
## Name: Asim Puri
## Date: 11/30/2023
##--------------------------------------------------------------


phonebook = {'Laura': ['Collins','231 Hull Rd','128-8596'],
             'Johnny': ['Jones','574 W 91st ave', '118-8517'],
             'Brian': ['Dixon','1903 Hillsborough St', '234-5678'],
             'Ella': ['Truffen','2110 Blue Ridge Rd', '901-2345'],
             'Nicole': ['Rambo','3801 Hillsborough St', '678-9123'],
             'Sakura': ['English','1 Sawamatsukura Nihommatsu', '345-7890'],
             'Soluna': ['Ward','50088 Kuala Lumpur', '456-1234'],
             'Ashton': ['Steckbeck','609 Fort Fisher Blvd S', '789-0123'],
             'Abi': ['Wilson','2201 NC-24, NC-87', '210-9876'],
             'Asim': ['Galvan','1103 Delham Rd', '543-2109']}



def showKey():
    print("Dictionary \'employees\' keys & values...\n")
    print(">Keys<<>>Values<")
    for key in phonebook:
        print(key, phonebook[key])
    print("-------------------------------------------------------")

def lookupAddress(msg):
    print(msg)

    print("\nChoose a person to look up:")
    showKey()
    name = input("Enter a name to look up: ")

    value = phonebook.get(name, 'Name not found')
    print(value,'\n') 

def DeleteRecord(msg):
    print(msg)
    showKey()
    name = input("Enter a name to delete: ")
    if name in phonebook:
        print(phonebook[name])
        confirm = input("Are you sure y/n: ")
        if confirm.lower == 'y':
            del phonebook[name]
    else:
        print("Name not found\n")
    showKey()

def CountEntries(msg):
    print(msg)
    num = len(phonebook)
    print("\nNumber is " + str(num))
    input("press any key to go on")
    print()

def AddNewRecord(msg):
    print(msg)
    name = input("Enter a first name: ")
    lName = input("Enter last name: ")
    phone = input("Enter a phone number: ")
    address = input("Enter a address: ")
    printString = ('[\''+lName+'\', \''+address+'\', \''+phone+'\']')
    phonebook[name] = printString
    showKey()

def UpdateRecord(msg):
    print(msg)
    showKey()
    name = input("Enter a first name: ")
    lName = input("Enter last name: ")
    phone = input("Enter a phone number: ")
    address = input("Enter a address: ")
    printString = ('[\''+lName+'\', \''+address+'\', \''+phone+'\']')
    phonebook[name] = printString
    print('\n',name, phonebook[name],'\n')


def menu():
    menuString = """Welcome to your rolodex
Choose from the following:
    1) Lookup address/phone
    2) Add new address/phone
    3) Update record
    4) Delete Record
    5) Count of Addresses
    0) ***To exit***"""
    choice = None

    while (choice != "0"):
        print(menuString)
        choice = input("Enter a choice -0- to exit: ")
        if choice =="1":
            lookupAddress(">>>>>>>>>>>>>>>     Lookup Address   <<<<<<<<<<<<<<<<<<<")
        elif choice == "2":
            AddNewRecord(">>>>>>>>>>>>>>>>     Add New Record    <<<<<<<<<<<<<<<<<<<")
        elif choice == "3":
            UpdateRecord(">>>>>>>>>>>>>>>>     Update Record    <<<<<<<<<<<<<<<<<<<")
        elif choice == "4":
            DeleteRecord(">>>>>>>>>>>>>>>>     Delete Record    <<<<<<<<<<<<<<<<<<<")
        elif choice == "5":
            CountEntries(">>>>>>>>>>>>>>>>     Count number of entries    <<<<<<<<<<<<<<<<<<<")
        elif choice == "0":
            input("Press any key to exit")
            exit()
        else:
            print("*****Invalid Option***** \nTry again\n")


menu()