import unittest

def remainder(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return dividend % divisor

class TestRemainder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 7), 6)
        self.assertEqual(remainder(100, 25), 0)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), -1)
        self.assertEqual(remainder(-20, 7), -6)
        self.assertEqual(remainder(-100, 25), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ZeroDivisionError):
            remainder(10, 0)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 5), 0)
        self.assertEqual(remainder(0, -3), 0)

if __name__ == '__main__':
    unittest.main()