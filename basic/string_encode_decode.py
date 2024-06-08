"""
["neet","code","love","you"] -> "4:neet4:code4:love3:you"
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + ":" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            l = ""
            while s[i] != ":":
                l += s[i]
                i += 1

            res.append(s[i + 1 : i + int(l) + 1])
            i = i + int(l) + 1

        return res
