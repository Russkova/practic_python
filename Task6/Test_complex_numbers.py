import unittest
from complex_numbers import Complex


class TestComplex(unittest.TestCase):

    def test_add(self):
        complex1 = Complex(1, -3)
        complex2 = Complex(0, 7)
        expected = Complex(1, 4)
        actual = complex1+complex2
        self.assertEqual(expected, actual)

    def test_add_with_zero(self):
        complex1 = Complex(1, -3)
        complex2 = Complex(-1, 3)
        expected = Complex()
        actual = complex1 + complex2
        self.assertEqual(expected, actual)

    def test_sub(self):
        complex1 = Complex(1, -3)
        complex2 = Complex(6, 3)
        expected = Complex(-5, -6)
        actual = complex1 - complex2
        self.assertEqual(expected, actual)

    def test_mul(self):
        complex1 = Complex(1, 4)
        complex2 = Complex(3, 3)
        expected = Complex(-9, 15)
        actual = complex1 * complex2
        self.assertEqual(expected, actual)


    def test_mul_with_zero(self):
        complex1 = Complex(1, 4)
        complex2 = Complex()
        expected = Complex()
        actual = complex1 * complex2
        self.assertEqual(expected, actual)

    def test_truediv(self):
        complex1 = Complex(1, 4)
        complex2 = Complex(2, 1)
        expected = Complex(1.2, 1.4)
        actual = complex1 / complex2
        self.assertEqual(expected, actual)

    def test_abs(self):
        complex1 = Complex(3, 4)
        expected = 5
        actual = abs(complex1)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    TestComplex()