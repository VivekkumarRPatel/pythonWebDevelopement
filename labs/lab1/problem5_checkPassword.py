import getpass 

'''
Here I have used getpass to make sure password is not visible 
on the console when user starts typing ! haha secret
'''

while True:
    pswd=getpass.getpass("Please provide your password")
    if pswd=="secret":
        print("Access granted")
        break
    else:
        print("Access denied")

