import unittest
from insertion_sort import sum


class SumTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
