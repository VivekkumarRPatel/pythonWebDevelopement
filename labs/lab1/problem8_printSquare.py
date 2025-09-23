'''
Problem Statement

Write a program that asks the user for a number and prints 
its square. Keep asking until the user types "0".
'''

while True:
    user_input=int(input("Please provide the number of your choice"))
    if user_input==0:
        print("Closing the program")
        break
    print("Square of the number is ",user_input*user_input, end="")
    print()
