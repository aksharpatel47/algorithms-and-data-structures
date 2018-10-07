from typing import List
from collections import Counter


def sort_array_with_max_given(input_list: List[int], max: int) -> List[int]:
    counts = Counter()

    for num in input_list:
        counts[num] += 1

    result = []

    for i in range(max + 1):
        result.extend([i] * counts[i])

    return result
