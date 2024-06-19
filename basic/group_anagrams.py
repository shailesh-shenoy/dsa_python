from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_map = {}
        
        for s in strs:
            temp = [0] * 26 
            for c in s:
                s_index = ord(c) - ord("a")
                temp[s_index] += 1

            tup = tuple(temp)
            if tup not in count_map:
                count_map[tup] = []
            count_map[tup].append(s)
        
        return count_map.values()
