#!/usr/bin/python3
"""just a test module
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestCaseMaxInteger(unittest.TestCase):
    """just a class with test cases"""

    def test_max_int(self):
        """correct test"""
        lst = [10, 0, 5, 6]
        self.assertEqual(max_integer(lst), 10)
        lst = [1, 2, 3, 4]
        self.assertEqual(max_integer(lst), 4)
        lst = [-4, 1, 5, 7]
        self.assertEqual(max_integer(lst), 7)
        lst = [30]
        self.assertEqual(max_integer(lst), 30)
        lst = [None]
        self.assertEqual(max_integer(lst), None)
        lst = []
        self.assertEqual(max_integer(lst), None)
        lst = [1, 3, -float('inf'), 2]
        self.assertEqual(max_integer(lst), 3)
        lst = [8, 9, 400, float('inf')]
        self.assertEqual(max_integer(lst), float('inf'))
        lst = [-19, -36, -17, -1]
        self.assertEqual(max_integer(lst), -1)

    def test_types(self):
        """just function for
        type testing"""
        lst = ['nic', 5, 3]
        self.assertRaises(TypeError, max_integer, lst)
        lst = None
        self.assertRaises(TypeError, max_integer, lst)
