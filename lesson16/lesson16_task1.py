import time


class ReworkEnumerate:

    def __init__(self, iterable, start=0):
        self.ind = 0
        if start != 0:
            self.ind = start
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iterable) > self.ind:
            var = (self.iterable[self.ind])
            val = (self.iterable.index(var), var)
            self.ind += 1
        else:
            raise StopIteration
        time.sleep(1)
        return val


tipo_enumerate = ReworkEnumerate([23, 24, 74, 2242, 53456, 4, 634, 6], 3)

for i in tipo_enumerate:
    print(i)
