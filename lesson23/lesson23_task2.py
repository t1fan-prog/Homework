def is_palindrome(looking_str: str, index: int = 0) -> bool:
    revers_index = -1 - index
    if index == round(len(looking_str)/2):
        return True
    elif looking_str[index] == looking_str[revers_index]:
        return is_palindrome(looking_str, index+1)
    else:
        return False


print(is_palindrome('аргентинецценитнегра'))
