from .binary_search import search
from unittest import TestCase


class BinarySearchTest(TestCase):
    def test_bin_search(self):
        self.assertEqual(search([1], 1), True)
        self.assertEqual(search([2], 1), False)
        self.assertEqual(search([1, 2], 1), True)
        self.assertEqual(search([1, 2], 3), False)
        self.assertEqual(search([1, 2, 3, 4, 5], 3), True)
        self.assertEqual(search([1, 2, 3, 4, 5], 6), False)
