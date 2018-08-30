from typing import List


def sort(values: List[int]) -> List[int]:
    for j in range(1, len(values)):
        key = values[j]

        i = j - 1

        while i >= 0 and values[i] > key:
            values[i + 1] = values[i]
            i -= 1

        values[i + 1] = key

    return values
