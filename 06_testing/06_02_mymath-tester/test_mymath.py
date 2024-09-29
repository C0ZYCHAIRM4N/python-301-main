# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import unittest
from mymath import subtract_divide


class TestSubtractDivide(unittest.TestCase):

    def test_subtract_divide(self):
        self.assertEqual(subtract_divide(20, 10, 5), 4)  # Adjust the expected value if needed

    def test_subtract_divide_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            subtract_divide(20, 10, 0)  # Test for zero division

if __name__ == "__main__":
    unittest.main(verbosity=2)
  

