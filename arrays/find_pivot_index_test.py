from typing import List
import pytest
from .find_pivot_index import Solution


@pytest.mark.parametrize("test_input,expected", [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1), ([2, 1, -1], 0)])
def test_find_pivot(test_input: List[int], expected: int):
    s = Solution()
    assert s.pivotIndex(test_input) == expected
