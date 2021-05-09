class Mathematician:
    @staticmethod
    def square_nums(l_list):
        return [i**2 for i in l_list]

    @staticmethod
    def remove_positives(l_list):
        return [i for i in l_list if i < 0]

    @staticmethod
    def filter_leaps(l_list):
        return [i for i in l_list if i % 4 == 0]


m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

