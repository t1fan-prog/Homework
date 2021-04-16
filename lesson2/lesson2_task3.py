print("Weclome to Python calculator :D")

operation = str(input("Which operation are you going to use? Print:\n"
      "'a' for 'Addition'\n's' for 'Subtraction'\n'd' for 'Division'\n'm' for 'Multiplication'\n"
      "'e' for 'Exponent'\n'mod' for 'Modulus'\n'f' for 'Floor division'\n "))


first_number = float(input("Enter first integer of float number:\n"))

second_number = float(input("Enter second integer of float number:\n"))

if operation == "a":
    print(f"Result {first_number + second_number}")
elif operation == "s":
    print(f"Result {first_number - second_number}")
elif operation == "d":
    print(f"Result {first_number / second_number}")
elif operation == "m":
    print(f"Result {first_number * second_number}")
elif operation == "e":
    print(f"Result {first_number ** second_number}")
elif operation == "mod":
    print(f"Result {first_number % second_number}")
elif operation == "f":
    print(f"Result {first_number // second_number}")
else:
    print("You haven't chosen right option in the first step. Try again")