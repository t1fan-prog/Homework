def stop_words(words: list):
    def test(func):
        def wrap_func(*args):
            args_list = func(*args).split()
            for i in args_list:
                if i in words:
                    args_list[args_list.index(i)] = "*"
            result = " ".join(args_list)
            return result
        return wrap_func
    return test


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW"


a = create_slogan("Steve")
print(a)
