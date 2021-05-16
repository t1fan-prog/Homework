from random import randint


def lottery(number):

    local_number = randint(1, 3)
    print(local_number)

    def won_million():
        print("You won million")

    def won_nothing():
        print("You won nothing")

    if number == local_number:
        return won_million
    else:
        return won_nothing


user_choice = int(input("Choose number from 1 to 3\n"))

result = lottery(user_choice)

result()
