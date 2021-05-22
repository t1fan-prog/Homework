class IterObj:

    def __init__(self, *args):
        self.values = list(args)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError("There is no element with such an index")


a = IterObj(3, 32423, 23, 63, 2, 3674568, 32, 3, 23)
print(a[5486])
