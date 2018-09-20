from typing import List


def sort(values: List[int]) -> List[int]:
    """Sorts the values array using merge sort algorithm"""
    if len(values) < 2:
        return values

    split_index = len(values) // 2

    left_part = values[:split_index]
    right_part = values[split_index:]

    sorted_left_part = sort(left_part)
    sorted_right_part = sort(right_part)

    sorted_values = []

    while len(sorted_values) < len(values):
        if len(sorted_left_part) >= 1 and (len(sorted_right_part) == 0 or sorted_left_part[0] < sorted_right_part[0]):
            sorted_values.append(sorted_left_part.pop(0))
        else:
            sorted_values.append(sorted_right_part.pop(0))

    return sorted_values
