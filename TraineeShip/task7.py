import random

def playGame():
    bot = ["rock","paper","scissor"]

    result = random.choice(bot)

    options = ['rock','paper' , 'scissor']

    print("Let's Start the game. choose and type 'rock' or 'paper' or 'scissor' to begin the game")
    
    userChoice = input()
    
    if(userChoice in options):
            if(result == "rock"):
                print("Computer Chose Rock!")
            if(result == "paper"):
                print("Computer Chose Paper")
            if(result == "scissor"):
                print("Computer Chose Scissor")
       
    else:
        print("Type or choose 'rock','paper','scissor' .")


    if(userChoice == "rock" and result == "paper" ):
        print("You lost")
    elif(userChoice == "rock" and result == "scissor" ):
        print("You Won!")
    elif(userChoice == "paper" and result == "scissor"):
        print("You lost")
    elif(userChoice == "paper" and result == "rock"):
        print("You Won!")
    elif(userChoice == "scissor" and result == "rock"):
        print("You lost")
    elif(userChoice == "scissor" and result == "paper"):
        print("You Won!")
    else:
        print("Nobody Won !")
           


playGame()





