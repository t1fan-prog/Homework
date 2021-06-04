from module import add
from random import randint


def simple_adder():
    first = randint(-9999999999999999999999, 9999999999999999999999)
    second = randint(-9999999999999999999999, 9999999999999999999999)

    result = add(first, second)

    return result


print(f"If it's '0' I'll give you 1000$ :)\n{simple_adder()}")
