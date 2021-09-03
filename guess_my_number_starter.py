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
import random
computer_number= random.randint(1,99)
guess=None 
print("     Guess my number\n     It's between [1 -99]")
while guess!= computer_number:
    guess=int(input('Enter Your Number: '))
    if guess < computer_number:
        print("Sorry your guess is too low ...\n Try again ")
        continue
    elif guess >computer_number:
        print("sorry your guess is too high ...\n Try again ")
        continue
    elif guess==computer_number:
        print("Hurray !!! you guessed the number.")
        print("The number was ",computer_number)
       
        
