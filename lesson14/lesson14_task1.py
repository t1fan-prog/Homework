def logger(func):
    def wrap_func(*args):
        str_arg_list = [str(i) for i in args]
        arguments = ", ".join(str_arg_list)
        print(f'{func.__name__} called with {arguments}')
    return wrap_func


@logger
def add(x, y):
    return x + y


@logger
def multi(x, y):
    return x * y


@logger
def subs(x, y):
    return x - y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
multi(2, 10)
subs(23, 22)
square_all(1, 2, 3)
