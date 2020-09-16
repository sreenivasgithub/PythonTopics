import unittest
from . arith import addition, division


class TestArithmetic(unittest.TestCase):
    def test_addition_with_integers(self):
        result = addition(3, 4)
        excepted = 7
        self.assertEqual(result, excepted)

    def test_addition_with_strings(self):
        result = addition('vinod', 'kumar')
        excepted = 'vinodkumar'
        self.assertEqual(result, excepted)

    def test_addition_with_different_types(self):
        #self.assertRaises(addition(2, '4'), TypeError)
        result = addition('3', 4)
        excepted = 'please enter integers'
        self.assertEqual(result, excepted)


class testDivision(unittest.TestCase):
    def test_division_with_integers(self):
        result = division(10, 2)
        excepted = 5
        self.assertEqual(result, excepted)

    def test_division_with_zero(self):
        result = division(10, 0)
        expected = 'ZeroDivisionError'
        self.assertEqual(result, expected)

    def test_division_with_strings(self):
        result = division('s', 'v')
        excepted = 'error'
        self.assertEqual(result, excepted)

    def test_division_with_different_arg(self):
        result = division(2, '3')
        excepted = 'error'
        self.assertEqual(result, excepted)