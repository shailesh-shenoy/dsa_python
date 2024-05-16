from collections import defaultdict
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    frq = defaultdict(int)
    for n in nums:
        frq[n] += 1

    frq_list = [(f * -1, key) for key, f in frq.items()]
    heapq.heapify(frq_list)

    result = []
    for i in range(k):
        if not frq_list:
            break
        result.append(heapq.heappop(frq_list)[-1])

    return result


def topKFrequentOptimized(nums: List[int], k: int) -> List[int]:
    frq = {}
    for n in nums:
        frq[n] = frq.get(n, 0) + 1

    count_list = [0] * (len(nums) + 1)
    for n, f in frq.items():
        if count_list[f] == 0:
            count_list[f] = [n]
        else:
            count_list[f].append(n)

    result = []
    for i in range(len(count_list) - 1, 0, -1):
        if not count_list[i]:
            continue
        for n in count_list[i]:
            result.append(n)
            if len(result) >= k:
                return result

    return result


if __name__ == "__main__":
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequent([1], 1))  # [1]
    print(topKFrequent([1, 2], 2))  # [1, 2]
    print(topKFrequent([1, 2, 10, 4, 1, 5, 6, 7, 7, 8, 9, 10, 7], 3))  # [1, 2, 3]
    print(topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 2))  # [3, 1]
    print(topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 1))  # [3]
    print(topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 3))  # [3, 1, 2]
    print(topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 4))  # [3, 1, 2]

    print("Optimized")

    print(topKFrequentOptimized([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequentOptimized([1], 1))  # [1]
    print(topKFrequentOptimized([1, 2], 2))  # [1, 2]
    print(
        topKFrequentOptimized([1, 2, 10, 4, 1, 5, 6, 7, 7, 8, 9, 10, 7], 3)
    )  # [1, 2, 3]
    print(topKFrequentOptimized([1, 1, 1, 2, 2, 3, 3, 3, 3], 2))  # [3, 1]
    print(topKFrequentOptimized([1, 1, 1, 2, 2, 3, 3, 3, 3], 1))  # [3]
    print(topKFrequentOptimized([1, 1, 1, 2, 2, 3, 3, 3, 3], 3))  # [3, 1, 2]
    print(topKFrequentOptimized([1, 1, 1, 2, 2, 3, 3, 3, 3], 4))  # [3, 1, 2]
