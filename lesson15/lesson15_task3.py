from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(f):
        @wraps(f)
        def wrapper(*args):
            try:
                return int(*args)
            except Exception:
                raise Exception("Enter only digits")
        return wrapper

    @staticmethod
    def to_str(f):
        @wraps(f)
        def wrapper(*args):
            return str(*args)
        return wrapper

    @staticmethod
    def to_bool(f):
        @wraps(f)
        def wrapper(*args):
            return bool(*args)
        return wrapper

    @staticmethod
    def to_float(f):
        @wraps(f)
        def wrapper(*args):
            try:
                return float(*args)
            except Exception:
                raise Exception("Enter only digits")

        return wrapper


# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
# a = do_nothing("2dgs5")

# @TypeDecorators.to_str
# def do_nothing(var):
#     return var

# @TypeDecorators.to_bool
# def do_nothing(var):
#     return var

@TypeDecorators.to_float
def do_nothing(var):
    return var


a = do_nothing("24245")
print(a)
