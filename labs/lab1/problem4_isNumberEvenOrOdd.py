'''
Problem Statement

 Write a program that asks the user for a number and 
 determines if it is even or odd. Keep asking until 
 the user types -1.

'''


input_number=int(input("Please provide a number"))

while input_number!=-1:
    if input_number%2==0:
        print("Number is even")
    else:
        print("Number is odd")
    input_number=int(input("Please provide a number"))
print("Closing the program")    