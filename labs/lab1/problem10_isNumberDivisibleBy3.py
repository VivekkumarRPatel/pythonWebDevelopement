'''
Problem Statement

Write a program that asks the user for a number and 
prints whether it is divisible by 3. 
Keep asking until the user types -1.

'''


while True:
    user_input=int(input("Please enter a number of your choice"))
    if user_input==-1:
        print("!! Oops Closing the program.")
        break

    if user_input%3==0:
        print("The number is divisible by 3")
    else :
        print("The number is no divisible by 3")    
