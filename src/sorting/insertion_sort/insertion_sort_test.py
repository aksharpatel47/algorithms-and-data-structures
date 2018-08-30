from insertion_sort import sort
import unittest


class InsertionSortTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(sort(
            [5, 2, 4, 6, 1, 3]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
