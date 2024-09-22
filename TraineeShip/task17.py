# CLI quiz application in python

import random


print("Welcome to Python quiz game! You will be given 5 randomn questions")
print("---Let's get started---")


questions = [
     {
        "Question" : "What is the capital of France?",
        "answer" : "Paris",
        "option1" : "Russia",
        "option2" : "kathmandu"
        
    },
     {
         "Question" : "What is the largest planet in our solar system?",
         "answer" : "Jupiter",
         "option1" : "Milkyway",
         "option2" : "Venus"
     },
     {
         "Question" : "How many continents are there on Earth?",
         "answer" : "206",
         "option1" : "300",
         "option2" : "192"
     },
     {
         "Question" : "In which country is the Great Wall of China located?",
         "answer" : "China",
         "option1" : "Korea",
         "option2" : "Israel"
     },
     {
         "Question" : "What is the chemical symbol for water?",
         "answer" : "h2o",
         "option1" : "ho2",
         "option2" : "h3o"
     },
     {
         "Question" : "Which ocean is the largest in the world?",
         "answer" : "Pacific",
         "option1" : "Atlantis",
         "option2" : "Arctic"
     }
]

score = 0

for i in range(len(questions)):
    print(questions[i]["Question"])
    print(questions[i]["option1"])
    print(questions[i]["option2"])
    print(questions[i]["answer"])
    
    print("answer:" ,end="")
    answer = input()
    
    if(answer == questions[i]["answer"]):
        score = score+1

print(f"Your score is {score} out of {len(questions)} ")
    
