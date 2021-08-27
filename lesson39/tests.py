import unittest
from lesson39_task1_task2 import *


class TestSQLAlchemy(unittest.TestCase):

    def test_name_surname(self):
        self.assertIsNotNone(name_surname())
        self.assertIn('Alana Walsh', name_surname())
        self.assertIn('Tomas Vermalen', name_surname())
        self.assertIn('Steven King', name_surname())

    def test_surname_and_department(self):
        self.assertIsNotNone(surname_and_department())
        self.assertIn('Renske Ladwig, 50', surname_and_department())
        self.assertIn('Winston Taylor, 50', surname_and_department())
        self.assertIn('Peter Vargas, 50', surname_and_department())
        self.assertIn('Tomas Vermalen, 90', surname_and_department())

    def test_fourth_query(self):
        self.assertIsNotNone(fourth_query())
        self.assertIn('Martha, Sullivan, Shipping, South San Francisco, California', fourth_query())
        self.assertIn('Timothy, Gates, Shipping, South San Francisco, California', fourth_query())
        self.assertIn('Samuel, McCain, Shipping, South San Francisco, California', fourth_query())
        self.assertIn('Pat, Fay, Marketing, Toronto, Ontario', fourth_query())

    def test_fifth_query(self):
        self.assertIsNotNone(fifth_query())
        self.assertIn('Nanette, Cambrault, 80, Sales', fifth_query())
        self.assertIn('William, Smith, 80, Sales', fifth_query())
        self.assertIn('Charles, Johnson, 80, Sales', fifth_query())
        self.assertIn('Lisa, Ozer, 80, Sales', fifth_query())

    def test_seventh_query(self):
        self.assertIsNotNone(seventh_query())
        self.assertIn('Susan, Mavris, 6500.00', seventh_query())

    def test_eight_query(self):
        self.assertIsNotNone(eighth_query())
        self.assertIn('Finance, 6', eighth_query())
        self.assertIn('Human Resources, 1', eighth_query())
        self.assertIn('Sales, 34', eighth_query())

    def test_ninth_query(self):
        self.assertIsNotNone(ninth_query())
        self.assertIn('President, 24000.0', ninth_query())
        self.assertIn('Stock Clerk, 2785.0', ninth_query())
        self.assertIn('Public Relations Representative, 10000.0', ninth_query())

    def test_tenth_query(self):
        self.assertIsNotNone(tenth_query())
        self.assertIn('Sales Representative, Jonathon, Taylor, 3400.00', tenth_query())
        self.assertIn('Shipping Clerk, Sarah, Bell, 1500.00', tenth_query())
        self.assertIn('Public Accountant, William, Gietz, 700.00', tenth_query())
        self.assertIn('Programmer, Tomas, Vermalen, -33500.00', tenth_query())