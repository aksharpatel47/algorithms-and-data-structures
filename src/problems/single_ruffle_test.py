from unittest import TestCase
from .single_ruffle import is_single_ruffle


class SingleRuffleTest(TestCase):
    def test_is_single_ruffle(self):
        deck = [1, 3, 2, 4]
        half1 = [1, 2]
        half2 = [3, 4]
        with self.subTest(half1=half1, half2=half2):
            self.assertTrue(is_single_ruffle(deck, half1, half2))
        half1 = []
        half2 = [1, 3, 2, 4]
        with self.subTest(half1=half1, half2=half2):
            self.assertTrue(is_single_ruffle(deck, half1, half2))
        half1 = [1, 3, 2, 4]
        half2 = []
        with self.subTest(half1=half1, half2=half2):
            self.assertTrue(is_single_ruffle(deck, half1, half2))
