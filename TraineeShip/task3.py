print("Enter the first number:")
firstNumber = float(input())

print("Enter: + , - , /, * ")

operator = input()

secondNumber = float(input())

if(operator == "+"):
   result = firstNumber+secondNumber

if(operator == "-"):
   result =  firstNumber-secondNumber

if(operator == "/"):
   result =  firstNumber/secondNumber

if(operator == "*"):
   result =  firstNumber*secondNumber


print(f"The result is :{result}")