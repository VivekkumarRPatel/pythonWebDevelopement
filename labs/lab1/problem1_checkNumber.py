

'''
Problem Statement
Write a program that asks the user for a number and 
checks if it is positive, negative, or zero. Print the result.

'''


number=int(input("Please enter the number of your choice   0"))
if number==0:
    print("The number is Zero" , number)
elif number>0:
    print("The number is Positive", number)
else:
    print("The number is negative ", number)
