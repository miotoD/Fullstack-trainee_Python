toDoList = []

def showList():
    print("Your To do list for today ")
    print(toDoList)
    if(len(toDoList)==0):
        print("You have nothing in your wishlsit. Add something to it.")


def add():
    print("What do you want to add?")
    toDo = input()
    toDoList.append(toDo)
    print("Succesfully added")

def delete():
    print("Enter task you want to delete")
    deleteTask = input()
    if(deleteTask in toDoList):
        toDoList.remove(deleteTask)
        print("Task successfully deleted")


while(True):
    print("You can type 'viewlist' to view to do list , 'add' to add, 'delete' to delete. ")
    action = input()
    if(action == "viewlist"):
        showList()
    if(action == "add"):
        add()
    if(action == "delete"):
        delete()


