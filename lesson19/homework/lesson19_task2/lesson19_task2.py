import unittest
from lesson19.homework.lesson19_task1.lesson19_task1 import MyOpenFunc


class MyTestCase(unittest.TestCase):
    def test_counter(self):
        for i in range(3):
            with MyOpenFunc('phonebook.json') as f:
                f.read()
        self.assertEqual(3, MyOpenFunc.counter())

    def test_is_not_exist(self):
        def open_test():
            with MyOpenFunc('test.json') as f:
                f.read()

        with self.assertRaises(FileNotFoundError):
            open_test()

    def test_add_agr(self):
        def open_test():
            with MyOpenFunc('phonebook.json', 'r') as f:
                f.read()

        with self.assertRaises(TypeError):
            open_test()

    def test_data_check(self):
        with open("phonebook.json") as f:
            a = f.read()

        def open_test():
            with MyOpenFunc('phonebook.json') as f:
                return f.read()

        self.assertEqual(a, open_test())


if __name__ == '__main__':
    unittest.main()
