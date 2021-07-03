def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit():
        if len(digit_string) == 1:
            return int(digit_string)
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])
    else:
        raise ValueError("input string must be digit string")


print(sum_of_digits('34468568'))
