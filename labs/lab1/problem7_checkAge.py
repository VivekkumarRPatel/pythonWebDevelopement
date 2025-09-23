'''
Problem Statement

Create a program that asks the user for their age and 
prints whether they are a minor, an adult, 
or a senior (age >= 65). 
Keep asking until the user types "quit".


'''

while True:
    user_input=input("Please provide your age")
    if user_input.strip()=="quit" or user_input.strip()=="Quit":
        break
    age=int(user_input)
    if age >0 and age<=17:
        print("You are minor")
    elif age>=18 and age<=64 :
        print("You are adult")
    elif age>=65 : 
        print("You are senior")
    