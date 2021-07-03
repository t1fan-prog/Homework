def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError('This function works only with positive integers')
    else:
        return a + mult(a, n-1)


print(mult(3, -2))
