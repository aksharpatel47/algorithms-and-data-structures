from typing import List


def search(values: List[int], item: int) -> bool:
    """
    Searches the values array to check if item exists using
    binary search algorithm. This search assumes the values
    array is sorted.    
    """
    if len(values) == 1:
        return item == values[0]

    split_index = len(values) // 2

    left_part = values[:split_index]
    right_part = values[split_index:]

    if left_part[len(left_part) - 1] >= item:
        return search(left_part, item)
    else:
        return search(right_part, item)
