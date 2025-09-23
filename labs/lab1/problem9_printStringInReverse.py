'''
Problem Statement

Create a program that asks the user for a word 
and prints it reversed. Keep asking 
until the user types "done".

'''

while True:
    user_input=input("Please provide the number of your choice")
    if user_input.strip()=="done" or user_input.strip()=="Done":
        break
    for index in range(len(user_input)-1,-1,-1):
        print(user_input[index]," ",end="")
    print()