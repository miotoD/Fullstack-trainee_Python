#Files in Python
#Contact Book

contactBook = "C:\\Users\\asus\\Desktop\\contacts.txt"
    
print("Welcome to Contact Book.")


print("Type 'add' for adding contact, 'edit' for editing and 'search' for searching.")


def addContact():
     print("Number:", end=" ")
     number = input()
     print("Name:", end=" ")
     name = input()
     
     with open(contactBook,"a") as file:
         file.writelines(f"{name} - {number} \n")
         print("Contact added Successfully!")
         
def editContact():
    print('Edit an existing contact')
    print("Enter name to update contact")
    contact = input()
    
def searchContact():
    print("Search an exsisting contact")
    print("Enter contact name:", end=" ")
    
    search = input()     
    
    contactFound = False
    
    with open(contactBook, "r") as file:
        contents = file.read()
        
        lines = contents.lower().split("\n")
        for names in lines:
            print("Yo chai names hai:",names)
            if(search.lower() in names):
                print("Contact Found")
                print(names)
                break
    
    
    
    
     
command = input()

if(command == "add"):
    addContact()
if(command == "search"):
    searchContact()