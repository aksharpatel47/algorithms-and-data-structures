from insertion_sort import insertion_sort
import unittest


class InsertionSortTest(unittest.TestCase):
    def test(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(
            [5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
