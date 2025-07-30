import unittest
from simple_calculator import SimpleCalculator

class test_class(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(2, 8), 10)

    def test_substraction(self):
        self.assertEqual(self.calc.subtract(7, 3), 4)
        self.assertEqual(self.calc.subtract(14, 3), 11)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(7, 3), 4)
        self.assertEqual(self.calc.multiply(14, 3), 11)

    def test_division(self):
        self.assertEqual(self.calc.divide(7, 3) 4)
        self.assertEqual(self.calc.divide(14, 0), None)