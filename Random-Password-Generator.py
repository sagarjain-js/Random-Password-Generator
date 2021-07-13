#!/usr/bin/python3
import random
import string

print('Welcome to the world of Passwords')
 
def switch():
    length = int(input('\nEnter the length of your Password: '))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbols = string.punctuation

    print("Please Select the characters you want in your password")
 
# This will guide the user to choose option
    print("Press 0 for combination of = lower case + upper case + number + symbols \n")
    print("press 1 for combination of = lower case + upper case + number \n ")
    print("press 2 for combination of = lower case + upper case \n ")
    print("Press 3 for combination of = lower case + number + symbols \n")
    print("Press 4 for combination of = upper case + number + symbols \n")
    print("Press 5 for combination of = lower case + number \n")
    print("Press 6 for combination of = upper case + number \n")
    print("Press 7 for only lower case characters \n")
    print("Press 8 for only upper case characters \n")
    print("Press 9 for only numbers \n")

 
# This will take option from user    
    option = int(input(" your option : "))

    def all():
        char = lower + upper + number + symbols
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)
 
    def lun():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)
 
    def lu():
        char = lower + upper
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def lns():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def uns():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)                

    def ln():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def un():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def l():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def u():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

    def n():
        char = lower + upper + number
        temp = random.sample(char,length)
        password = "".join(temp)
        print(password)

# If user enters invalid option then this method will be called 
    def default():
        print("Incorrect option")
 
# Dictionary Mapping
    dict = {
        0 : all,
        1 : lun,
        2 : lu,
        3 : lns,
        4 : uns,
        5 : ln,
        6 : un,
        7 : l,
        8 : u,
        9 : n,
 
    }
    dict.get(option,default)() # get() method returns the function matching the argument
 
 
switch() # Call switch() method
