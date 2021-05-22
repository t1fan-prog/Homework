class ReworkRange:

    def __init__(self, l_start, l_end, l_step=1):
        self.start = l_start
        self.end = l_end - 1
        self.step = l_step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        val = self.start
        self.start += self.step
        return val


tipo_range = ReworkRange(23, 65, 3)

for i in tipo_range:
    print(i)
