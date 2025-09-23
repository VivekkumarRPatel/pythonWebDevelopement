'''
Problem Statement

Write a program that asks the user for a sentence and 
prints the number of characters in the sentence. 
Keep asking until the user types "stop".
'''


while True:
    user_input=input("Please provide your value")
    if user_input=="stop" or user_input=="Stop":
        break
    print("The number of characters are ", len(user_input))