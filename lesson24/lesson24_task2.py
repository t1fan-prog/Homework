from lesson24_task1 import Stack

stack = Stack()


def is_balanced(sequence):
    is_good = True

    for i in sequence:
        if i in '({[':
            stack.push(i)
        elif i in ')}]':
            if stack.is_empty():
                is_good = False
                break
            open_bracket = stack.pop()
            if open_bracket == '(' and i == ')':
                continue
            if open_bracket == '{' and i == '}':
                continue
            if open_bracket == '[' and i == ']':
                continue
            is_good = False
            break

    if is_good and stack.size() == 0:
        return True
    else:
        return False


print(is_balanced('({()))'))
