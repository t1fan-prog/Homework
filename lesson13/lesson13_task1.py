def variable_count(func):
    return func.__code__.co_nlocals


def test():
    var1 = "test"
    var2 = 1
    var3 = 2


a = variable_count(test)
print(a)
