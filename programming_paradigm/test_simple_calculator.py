import unittest
from simple_calculator import SimpleCalculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0,0),0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,3),2)
        self.assertEqual(self.calc.subtract(2,0),2)
        self.assertEqual(self.calc.subtract(5,6),-1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 6), 30)
        self.assertEqual(self.calc.multiply(5, -6), -30)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(30, 6), 5)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(-30, 6), -5)












