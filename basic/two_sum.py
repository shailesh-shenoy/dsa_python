from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        complement = {}
        for i, v in enumerate(nums):
            if v in complement:
                return [complement[v], i]
            complement[target - v] = i
