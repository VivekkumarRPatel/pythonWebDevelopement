'''
Problem Statement

Write a program that asks the user for their name and 
prints it back with the first letter capitalized. 
Keep asking until the user types "exit".

'''


while True:
    name=input("Please provide your First Fame")
    if(name=="exit" or name=="Exit"):
        print("Exiting the program")
        break
    print("Okay your first Name is ",name.capitalize())





