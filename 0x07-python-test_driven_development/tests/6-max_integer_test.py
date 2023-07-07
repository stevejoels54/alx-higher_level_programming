#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """Tests for max_integer function"""

    def test_empty_list(self):
        """Test empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        """Test single element list"""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        """Test positive numbers"""
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test negative numbers"""
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test mixed positive and negative numbers"""
        result = max_integer([1, -3, 2, -4, 5])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        """Test duplicate numbers"""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_float_numbers(self):
        """Test float numbers"""
        result = max_integer([1.5, 2.5, 3.5])
        self.assertEqual(result, 3.5)

    def test_invalid_elements(self):
        """Test list with invalid elements"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])

        with self.assertRaises(TypeError):
            max_integer([1, 2, None])


if __name__ == '__main__':
    unittest.main()
