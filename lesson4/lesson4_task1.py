# The Guessing Game.
#
# Write a program that generates a random number between 1 and 10 and lets the user guess
# what number was generated. The result should be sent back to the user via a print statement.

import random

number = random.randint(1, 10)

choice = input("Program has been already generated random number. Try to guess this number. "
               "Enter number from 1 to 10:\n")

if choice.isdecimal():
    choice = int(choice)
    if choice >= 10:
        print("Number is more than 10")
    elif choice == number:
        print(f"Your result: {choice}. Computer result: {number}. Good job :)")
    else:
        print("Loser")
else:
    print("You have entered wrong symbol. Please enter an integer from 1 to 10!")
