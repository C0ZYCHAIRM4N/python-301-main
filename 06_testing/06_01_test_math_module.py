# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.
import unittest
import math

class TestMath(unittest.TestCase):

    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3, 4), 3)

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)
        self.assertEqual(math.sqrt(9), 3)
        self.assertAlmostEqual(math.sqrt(2), 1.41421356237, places=10)

if __name__ == '__main__':
    unittest.main()