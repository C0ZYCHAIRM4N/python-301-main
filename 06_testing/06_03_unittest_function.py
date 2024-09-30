# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width

import unittest

class TestCalculateArea(unittest.TestCase):

    def test_calculate_area_pass(self):
        # This test should pass
        self.assertEqual(calculate_area(5, 3), 15)

    def test_calculate_area_fail(self):
        # This test should fail
        self.assertEqual(calculate_area(5, 3), 10)

if __name__ == '__main__':
    unittest.main()

