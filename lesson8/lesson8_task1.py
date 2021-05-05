def oops():
    list_1 = [1, 1, 1, 1]
    print(list_1[24])


# Нормально отработает, так как функция oops() вызовет именно IndexError
def error_index():
    try:
        oops()
    except IndexError:
        print("Ошибочка вышла, нет такого элемента")


# Программа закрашится, так как функция oops() вызовет IndexError ошибку, а проверяем ошибку отсутствия ключа в словаре
def error_key():
    try:
        oops()
    except KeyError:
        print("Ошибочка вышла, нет такого элемента")


error_index()
error_key()
