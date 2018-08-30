from insertion_sort import sort
import unittest


class InsertionSortTest(unittest.TestCase):
    def test(self):
        arr = [5, 4, 3, 2, 1]
        arr2 = [5, 2, 4, 6, 1, 3]
        sort(arr)
        sort(arr2)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
        self.assertEqual(arr2, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
