from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    maxL = 0
    l = 0
    for i, n in enumerate(nums):
        if i == 0:
            l = 1
            continue
        if nums[i - 1] == n - 1:
            l += 1
            maxL = max(l, maxL)
            continue
        l = 1

    return maxL


def longestSubsequenceOptimized(nums: List[int]) -> int:
    numSet = set(nums)

    maxL = 0

    for n in numSet:
        if n - 1 in numSet:
            continue
        l = 1
        while n + l in numSet:
            l += 1
            maxL = max(maxL, l)

    return maxL


if __name__ == "__main__":
    print(longestConsecutive([100, 4, 200, 1, 3, 2, 1]))
    print(longestSubsequenceOptimized([100, 4, 200, 1, 3, 2, 1]))
    print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longestSubsequenceOptimized([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longestConsecutive([1, 2, 0, 1]))
    print(longestSubsequenceOptimized([1, 2, 0, 1]))
    print(longestConsecutive([1, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
    print(longestSubsequenceOptimized([1, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
