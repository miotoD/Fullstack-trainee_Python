#Number guessing game python

import random

def play():
    number = random.choice(range(1,100))


    print("Guess the number:",end="")

    userInput = int(input())


    if(userInput == number):  
        print(f"Computer chose {number}.")
        print("You Won!")
    else:
        print("Try again..")


print("Welcome to the game . Type 'play' to start the game.")

userInput = input()

if(userInput.lower() == "play"):
    play()