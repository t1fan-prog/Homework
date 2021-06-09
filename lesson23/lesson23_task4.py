def reverse(input_str: str) -> str:
    if input_str == "":
        return input_str
    return input_str[-1] + reverse(input_str[:-1])


print(reverse("hello"))
