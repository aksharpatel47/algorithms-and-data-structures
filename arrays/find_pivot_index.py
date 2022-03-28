from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums) - nums[0]

        for i in range(len(nums)):
            if sum_left == sum_right:
                return i
            
            sum_left += nums[i]
            if i + 1 < len(nums):
                sum_right -= nums[i + 1]

        return -1
        