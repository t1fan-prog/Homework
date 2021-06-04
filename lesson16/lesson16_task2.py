class ReworkRange:

    def __init__(self, l_start=0, l_end=0, l_step=1):
        if l_end > 0:
            self.start = l_start
            self.end = l_end
            self.step = l_step
        else:
            self.start = 0
            self.end = l_start
            self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        val = self.start
        self.start += self.step
        return val


tipo_range = ReworkRange(5)

for i in tipo_range:
    print(i)
