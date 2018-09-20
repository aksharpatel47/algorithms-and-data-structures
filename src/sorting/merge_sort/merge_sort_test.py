from .merge_sort import sort
from unittest import TestCase


class MergeSortTest(TestCase):
    def test_sort(self):
        self.assertEqual(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
