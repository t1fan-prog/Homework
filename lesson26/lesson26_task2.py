class FibonacciSearch:
    def __init__(self):
        self.i = 0
        self.p = 0
        self.q = 0
        self.stop = False

    @staticmethod
    def get_fibonacci_number(k):
        first_number = 0
        second_number = 1
        n = 0

        while n < k:
            temp_number = second_number
            second_number = first_number + second_number
            first_number = temp_number
            n += 1
        return first_number

    def start_init(self, sequence):
        self.stop = False
        k = 0
        n = len(sequence)

        while self.get_fibonacci_number(k + 1) < len(sequence):
            k = k + 1
        m = self.get_fibonacci_number(k + 1) - (n + 1)
        self.i = self.get_fibonacci_number(k) - m
        self.p = self.get_fibonacci_number(k - 1)
        self.q = self.get_fibonacci_number(k - 2)

    def up_index(self):
        if self.p == 1:
            self.stop = True
        self.i = self.i + self.q
        self.p = self.p - self.q
        self.q = self.q - self.p

    def down_index(self):
        if self.q == 0:
            self.stop = True
        self.i = self.i - self.q
        temp = self.q
        self.q = self.p - self.q
        self.p = temp

    def search(self, sequence, element):
        self.start_init(sequence)
        result_index = -1
        while not self.stop:
            if self.i < 0:
                self.up_index()
            elif self.i >= len(sequence):
                self.down_index()
            elif sequence[self.i] == element:
                result_index = self.i
                break
            elif element < sequence[self.i]:
                self.down_index()
            elif element > sequence[self.i]:
                self.up_index()
        return result_index


if __name__ == '__main__':
    seq = [-2, 0, 1, 4, 6, 10, 14, 15, 24, 356, 456, 6755]

    fs = FibonacciSearch()

    element = 15

    print(fs.search(seq, element))