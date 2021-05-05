# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).

def math():
    a = input("Введите первую цифру:\n")
    b = input("Введите вторую цифру:\n")
    return (int(a) ** 2) / int(b)


try:
    result = math()
    print(result)
except ValueError:
    print("Введён некорректный символ. В следующий раз вводи только числа.\n")
except ZeroDivisionError:
    print("На ноль делить нельзя, учи математику")
