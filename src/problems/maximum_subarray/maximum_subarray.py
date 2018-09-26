from typing import List


def maximum_subarray(prices: List[int]) -> (int, int):
    """
    Based on the given list of stock prices, find out on which
    day to buy and on which day to sell to get the maximum profit.
    """

    if len(prices) < 2:
        raise ValueError("Length of prices should be 2 or more.")

    max_diff = -1
    min_index = 0
    result = None

    for index in range(1, len(prices)):
        cur_diff = prices[index] - prices[min_index]
        if cur_diff > max_diff:
            max_diff = cur_diff
            result = (min_index, index)
        if prices[index] < prices[min_index]:
            min_index = index

    return result
