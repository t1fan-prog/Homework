import random

first_int = random.randint(1, 10)
second_int = random.randint(1, 10)
third_int = random.randint(1, 10)

result = (first_int - second_int) / third_int

user_answer = float(input(f"What is the result of the next expression: ({first_int}-{second_int})/{third_int} ?\n"))

if user_answer == result:
    print("Good job!")
else:
    print("Train your math.")
