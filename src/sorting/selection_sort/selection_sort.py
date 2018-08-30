from typing import List


def sort(values: List[int]):
    for i, val in enumerate(values):
        least_index = i
        for j in range(i, len(values)):
            if values[j] < values[least_index]:
                least_index = j

        values[i] = values[least_index]
        values[least_index] = val
