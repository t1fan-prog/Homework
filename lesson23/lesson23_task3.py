def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    elif n == 0:
        return 0
    else:
        return a + mult(a, n-1)


print(mult(3, 4))
