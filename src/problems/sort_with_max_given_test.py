from .sort_with_max_given import sort_array_with_max_given
import unittest


class SortWithMaxGivenTest(unittest.TestCase):
    def test_sort(self):
        arr = [5, 4, 3, 2, 1]
        max_num = 5
        s_arr = sort_array_with_max_given(arr, max_num)
        self.assertEqual(s_arr, [1, 2, 3, 4, 5])
