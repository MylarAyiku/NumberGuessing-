"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
#random number generation
random_number= random.randint(1,99)
#defining computers number
cnum=random_number
guess=None 
name=input("Please enter your name ").upper()
print(f" Hello {name} !\n  Welcome To Mylar's Guessing Game")
while cnum != guess:
    guess=int(input('Enter Your Number: '))
    if guess < random_number:
        print("Sorry your guess is too low ...\n Try again ")
        continue
    elif guess >random_number:
        print("sorry your guess is too high ...\n Try again ")
        continue
    elif guess==random_number:
        print("Hurray !!! you guessed the number.")
        print("Would you like to play again(y,n)")
        inp=input()
        if inp=='y' or'Y':
            continue 
        else:
            prin("THANK YOU ")
            break
          
          
