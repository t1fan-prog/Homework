def arg_rules(type_: type, max_length: int, contains: list):
    def test(func):
        def wrap_func(name):
            def check():
                """Проверяем наличие символов в аргументе"""
                try:
                    [name.index(i) for i in contains]
                    return True
                except ValueError:
                    return False

            rule1 = type(name) == type_
            rule2 = len(name) <= max_length
            rule3 = check()

            if not rule1:
                raise TypeError(f"Slogan must be {type_} type.")
            elif not rule2:
                raise Exception(f"Slogan must contain not more than {max_length} symbols.")
            elif not rule3:
                raise Exception(f"Slogan should contain {', '.join(contains)} symbols")
            else:
                return func(name)
        return wrap_func
    return test


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("S@SH04"))
