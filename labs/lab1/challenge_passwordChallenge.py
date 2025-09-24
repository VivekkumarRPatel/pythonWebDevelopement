'''
Problem Statement

# CHALLENGE
# create a loop that will keep prompting a user for a correct format password. 

# a correct format password must be 10 characters, 
# have one letter, one symbol, one capital letter,
#  one number.


'''
import string 

def is_valid_password(pswd):
    is_valid_length=len(pswd)==10
    has_digit=any(c.isdigit() for c in pswd)
    has_lower=any(c.islower() for c in pswd)
    has_upper=any(c.isupper() for c in pswd)
    has_special=any(c in string.punctuation for c in pswd)

    return is_valid_length and has_digit and has_lower and has_upper and has_special


while True:
    user_input=input("Please enter password in valid format")
    if is_valid_password(user_input):
       print("Good job, You entered password in correct format") 
       break
    else:
       print("Hmm You entered password in incorrecr format")



