from lesson16.lesson16_task3 import IterObj
import unittest


class TestIterObj(unittest.TestCase):

    def iterable(self):
        a = IterObj(3, 32423, 23, 63, 2, 3674568, 32, 3, 23)
        self.assertEqual(a[3], 63, "Test")
        self.assertRaises(IndexError, a[52414])
        self.assertEqual(list(a), [3, 32423, 23, 63, 2, 3674568, 32, 3, 23], "Seems it's not iterable")
        self.assertRaises(IterObj(a=23), TypeError)


if __name__ == '__main__':
    unittest.main()
