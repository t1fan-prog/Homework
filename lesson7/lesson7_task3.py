def make_operation(operation, *args):
    numbers = list(args)
    total = numbers[0]
    if operation == "+":
        for i in numbers[1:]:
            total += i
    elif operation == "-":
        for i in numbers[1:]:
            total -= i
    elif operation == "*":
        for i in numbers[1:]:
            total *= i
    return total


print(make_operation("*", 7, 6))
