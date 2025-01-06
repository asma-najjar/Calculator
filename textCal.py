import unittest
from calculator2 import Calculator2

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator2()

    # Test Addition
    def test_add(self):
        self.assertEqual(self.calc.operations['+'](10, 5), 15)
        self.assertEqual(self.calc.operations['+'](-1, 1), 0)
        self.assertEqual(self.calc.operations['+'](-1, -1), -2)
        self.assertEqual(self.calc.operations['+'](0, 0), 0)
        self.assertAlmostEqual(self.calc.operations['+'](1.5, 2.5), 4.0, places=6)

    # Test Subtraction
    def test_subtract(self):
        self.assertEqual(self.calc.operations['-'](3, 1), 2)
        self.assertEqual(self.calc.operations['-'](-1, 1), -2)
        self.assertEqual(self.calc.operations['-'](-1, -1), 0)
        self.assertAlmostEqual(self.calc.operations['-'](2.5, 1.0), 1.5, places=6)

    # Test Multiplication
    def test_multiply(self):
        self.assertEqual(self.calc.operations['*'](10, 5), 50)
        self.assertEqual(self.calc.operations['*'](-1, 1), -1)
        self.assertEqual(self.calc.operations['*'](-1, -1), 1)
        self.assertEqual(self.calc.operations['*'](0, 100), 0)
        self.assertAlmostEqual(self.calc.operations['*'](1.5, 2), 3.0, places=6)

    # Test Division
    def test_divide(self):
        self.assertEqual(self.calc.operations['/'](10, 5), 2)
        self.assertEqual(self.calc.operations['/'](-1, 1), -1)
        self.assertEqual(self.calc.operations['/'](-1, -1), 1)
        self.assertAlmostEqual(self.calc.operations['/'](5, 2), 2.5, places=6)
        with self.assertRaises(ValueError):
            self.calc.operations['/'](10, 0)

    # Test Complex Expressions (Option 5)
    def test_calculate_expression(self):
        self.assertEqual(self.calc.calculate_expression("1+2"), 3)
        self.assertEqual(self.calc.calculate_expression("10-5"), 5)
        self.assertEqual(self.calc.calculate_expression("10*5"), 50)
        self.assertEqual(self.calc.calculate_expression("10/5"), 2)
        self.assertAlmostEqual(self.calc.calculate_expression("1+2/3-7"), -5.333333333333333, places=6)
        self.assertAlmostEqual(self.calc.calculate_expression("2+3*4/2-5"), 3, places=6)
        self.assertEqual(self.calc.calculate_expression("(5+2)*3"), 21)
        self.assertAlmostEqual(self.calc.calculate_expression("(1+2)/(3-1)"), 1.5, places=6)
        self.assertEqual(self.calc.calculate_expression("(5+(2*3))"), 11)

    # Test Parentheses Validation
    def test_is_valid_parentheses(self):
        self.assertTrue(self.calc.is_valid_parentheses("(5+3)"))
        self.assertTrue(self.calc.is_valid_parentheses("((1+2)*3)"))
        self.assertFalse(self.calc.is_valid_parentheses("(5+3"))
        self.assertFalse(self.calc.is_valid_parentheses("(5+3))"))

    # Test Edge Cases
    def test_edge_cases(self):
        self.assertEqual(self.calc.calculate_expression("0+0"), 0)
        self.assertEqual(self.calc.calculate_expression("5*0"), 0)
        self.assertEqual(self.calc.calculate_expression("5/1"), 5)
        self.assertAlmostEqual(self.calc.calculate_expression("1/3"), 0.3333333333333333, places=6)

     # Test Invalid Inputs
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_expression("5++2")
        with self.assertRaises(ValueError):
            self.calc.calculate_expression("(5+2")
        with self.assertRaises(ValueError):
            self.calc.calculate_expression("")


if __name__ == "__main__":
    unittest.main()
