# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name = input("Hello. Please enter your name:\n")

while True:
    age = input("Please enter your age:\n")
    if age.isdecimal():
        age = int(age)
        print(f"Hello {name}, on your next birthday you'll be {age + 1} years")
        break
    print("Age shouldn't contain any additional symbols!\n")
