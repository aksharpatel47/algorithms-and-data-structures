from typing import List


def insertion_sort(values: List[int]) -> List[int]:
    for i, val in enumerate(values):
        least_index = i
        for j in range(i, len(values)):
            if values[j] < val:
                least_index = j

        values[i] = values[least_index]
        values[least_index] = val

    return values
