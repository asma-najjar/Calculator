import unittest
from calculator2 import Calculator2

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator2()

    def test_add(self):
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(10, 0), "Error: Division by zero is undefined")

    def test_anyMathExpression(self):
        self.assertEqual(self.calc.anyMathExpression("1+2"), 3)
        self.assertEqual(self.calc.anyMathExpression("10-5"), 5)
        self.assertEqual(self.calc.anyMathExpression("10*5"), 50)
        self.assertEqual(self.calc.anyMathExpression("10/5"), 2)
        self.assertAlmostEqual(self.calc.anyMathExpression("1+2/3-7"), -5.333333333333333, places=6)
        self.assertAlmostEqual(self.calc.anyMathExpression("2+3*4/2-5"), 3, places=6)
        self.assertEqual(self.calc.anyMathExpression("10/0"), "Error: Division by zero is undefined")

if __name__ == "__main__":
    unittest.main()
