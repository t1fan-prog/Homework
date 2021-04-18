user_string = input("Type a word:\n")

if len(user_string) < 2:
    print("Empty String")
else:
    print("Result: " + user_string[0:2] + user_string[-2:])
