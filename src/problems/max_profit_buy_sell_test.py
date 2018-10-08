from unittest import TestCase
from .max_profit_buy_sell import max_profit_buy_sell


class MaximumSubArrayTest(TestCase):
    def test_error_on_empty_input(self):
        with self.assertRaises(ValueError):
            max_profit_buy_sell([])

    def test_error_on_single_input(self):
        with self.assertRaises(ValueError):
            max_profit_buy_sell([1])

    def test_maximum_subarray(self):
        self.assertEqual(max_profit_buy_sell([1, 2]), (0, 1))
        self.assertEqual(max_profit_buy_sell([2, 1]), None)
        self.assertEqual(max_profit_buy_sell(
            [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]), (7, 11))
