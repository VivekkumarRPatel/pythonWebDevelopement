import getpass 

'''
Problem Statement
 Create a program that asks the user for a password. 
 If the password is "secret", print "Access granted". 
 Otherwise, print "Access denied" and keep asking until 
 the correct password is entered.

 
Here I have used "getpass" to make sure password is not visible 
on the console when user starts typing ! haha secret
'''

while True:
    pswd=getpass.getpass("Please provide your password")
    if pswd=="secret":
        print("Access granted")
        break
    else:
        print("Access denied")

