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
    print("Enter name to update contact")
    userInput = input()
    
    contactFound = False
    updatedContacts = []
    
    with open(contactBook,"r") as file:
        contents = file.read()
        lines = contents.split("\n")
                
        for contact in lines:  
            if userInput.lower() in contact.lower():  
                print("Contact exists:", contact)
                
                print("Edit the contact (name - number):", end=" ")
                updated = input()
                updatedContacts.append(f"{updated} \n")  # Add the updated contact to the list
                contactFound = True
            else:
                updatedContacts.append(f"{contact}\n")  
        
        if contactFound:
            with open(contactBook, "w") as file:
                file.writelines(updatedContacts)
                print("Contact updated successfully!")
        else:
            print("No such contact found.")
            
                   
        
                
    
def searchContact():
    print("Search an exsisting contact")
    print("Enter contact name:", end=" ")
    
    search = input()     
    
    found = False
        
    with open(contactBook, "r") as file:
        contents = file.read()
        
        lines = contents.lower().split("\n")
        
        for names in lines:
            if(search.lower() in names.lower()):
                print("Contact Found")
                print(names)
                break
    
    
    
     
command = input()

if(command == "add"):
    addContact()
if(command == "search"):
    searchContact()
if(command == "edit"):
    editContact()
