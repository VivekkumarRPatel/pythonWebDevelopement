#Create a while loop that prints all numbers divisible by 5 between 0 and 100.

number=0
print("Numbers divisble by 5 are: ")
while number<101:
    if(number%5==0):
        print(number, "  ",end="")
    number+=1