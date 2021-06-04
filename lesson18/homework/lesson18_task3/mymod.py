def count_lines(name):
    with open(name) as f:
        lines_quantity = len(f.readlines())
    return lines_quantity


def count_chars(name):
    with open(name) as f:
        char_quantity = len(f.read())
    return char_quantity


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    return f'File "{name}" contains {lines} lines and {chars} characters'


if __name__ == '__main__':
    print(test("phonebook.json"))
