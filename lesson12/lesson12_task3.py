class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction

    def __add__(self, other):
        if isinstance(other, Fraction):
            return self.fraction + other.fraction
        else:
            return "Не туда зашёл"

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return self.fraction - other.fraction
        else:
            return "Не туда зашёл"

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return self.fraction * other.fraction
        else:
            return "Не туда зашёл"

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self.fraction / other.fraction
        else:
            return "Не туда зашёл"


class Test:

    def __init__(self, value):
        self.value = value


x = Fraction(1/3)

y = Fraction(1/4)

z = Test(4)

print(x / y)
print(x / z)
