print("Welcome to Python calculator :D")

list_of_operations = ["a", 's', "d", "m", "e", "mod", "f"]


while True:
    operation = str(input("Which operation are you going to use? Print:\n"
                          "'a' for 'Addition'\n's' for 'Subtraction'\n'd' for 'Division'\n'm' for 'Multiplication'\n"
                          "'e' for 'Exponent'\n'mod' for 'Modulus'\n'f' for 'Floor division'\n "))
    if operation.lower() in list_of_operations:
        break
    print("Please enter a correct operation!\n")

while True:
    first_number = input("Enter first integer:\n")
    if first_number.isdigit():
        break
    print("Please enter a digit!\n")

while True:
    second_number = input("Enter second integer:\n")
    if second_number.isdigit():
        break
    print("Please enter a digit!\n")

first_number = int(first_number)
second_number = int(second_number)

if operation == "a":
    print(first_number + second_number)
elif operation == "s":
    print(first_number - second_number)
elif operation == "d":
    print(first_number / second_number)
elif operation == "m":
    print(first_number * second_number)
elif operation == "e":
    print(first_number ** second_number)
elif operation == "mod":
    print(first_number % second_number)
elif operation == "f":
    print(first_number // second_number)
