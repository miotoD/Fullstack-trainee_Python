# vocabulary flash_card Cli app in python 

flashcards = {}

#appending the files content to flashcard directory (if there is any).
with open("C:\\Users\\asus\\Desktop\\flashcard.txt","r+") as file:
    for items in file:
        ques,ans = items.strip().split(":")
        flashcards[ques] = ans

print("Weclome to the Flash Card python App")
print("======================================")



def add():    
    ques = input("Enter the question:")
    ans = input("Enter the answer:")
    
    flashcards.update({ques: ans})
    
    with open("C:\\Users\\asus\\Desktop\\flashcard.txt","a+") as file:
        file.write(f"{ques}: {ans} \n")
    
    print("-------------------------------")
    print("Flashcard added to the File!")      
    print("-------------------------------")
    
def view():
    number = 0
    with open("C:\\Users\\asus\\Desktop\\flashcard.txt","r+") as file:
    
        print("=========Flashcard Details===========")
        for flashcards in file:
            number = number+1
            print(f"{number} {flashcards}") 
        print("====================")

def delete():
    u_input = input("Enter the keywoard you want to delete:")
    
    if u_input in flashcards:
        flashcards.pop(u_input)
        print("Flashcard Succesfully deleted!")
        with open("C:\\Users\\asus\\Desktop\\flashcard.txt","w") as file:
            for items in flashcards:
                file.write(f"{items}: {flashcards[items]} \n")
    
    
    
    else:
        print("Flashcard doesnot exist")




      
            
while True:       
    print("=====Menu=====")
    print("1 Add flashcard")
    print("2 view flashcard")
    print("3 Delete flashcard")
    print("4 Exit")    
    
    
    user_input = input("Enter:")

    if(user_input == "1"):
        add()
    if(user_input == "2"):
        view()
    if(user_input == "3"):
        delete()
    if(user_input == "4"):
        break
 



