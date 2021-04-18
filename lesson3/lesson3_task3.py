import random
names = ["artem", "dereck", "hector", "john", "lisa"]

my_name = random.choice(names)

name = input("Try your luck and guess my name. You can win 10$ :)) You have 1 chance!\n"
             "So, your choice is:\n")

if my_name == name.lower():
    print("WTF? How is it possible???? Take your 10$")
else:
    print("You were so close, loser")
