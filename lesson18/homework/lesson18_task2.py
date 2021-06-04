import sys
import unittest


class TestSysPath(unittest.TestCase):

    def iterable(self):
        """При импорте модуля 'sys' поиск файлов будет происходить сначала в директории, которой находится
        файл, в котором импортнули 'sys', а потом уже в стандартных пакетах python"""
        a = sys.path
        self.assertEqual(a[0], '/home/t1fan/pythonCourse/lesson18', 'Что-то пошло не так с директорией))')


if __name__ == '__main__':
    unittest.main()
