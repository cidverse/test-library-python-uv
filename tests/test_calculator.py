from test_library_python_uv.calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
