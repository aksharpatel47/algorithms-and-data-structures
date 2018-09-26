from unittest import TestCase
from .maximum_subarray import maximum_subarray


class MaximumSubArrayTest(TestCase):
    def test_error_on_empty_input(self):
        with self.assertRaises(ValueError):
            maximum_subarray([])

    def test_error_on_single_input(self):
        with self.assertRaises(ValueError):
            maximum_subarray([1])

    def test_maximum_subarray(self):
        self.assertEqual(maximum_subarray([1, 2]), (0, 1))
        self.assertEqual(maximum_subarray([2, 1]), None)
        self.assertEqual(maximum_subarray(
            [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]), (7, 11))
