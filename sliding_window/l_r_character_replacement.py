class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frq = {}
        res = 0

        for r in range(len(s)):
            w_length = r - l + 1
            frq[s[r]] = frq.get(s[r], 0) + 1

            maxF = 0
            for v in frq.values():
                maxF = max(maxF, v)

            if w_length - maxF <= k:
                res = max(w_length, res)
                continue

            frq[s[l]] -= 1
            l += 1

        return res


if __name__ == "__main__":
    print(Solution().characterReplacement("ABAB", 2))  # 4
    print(Solution().characterReplacement("AABABBA", 1))  # 4
    print(Solution().characterReplacement("AABABBA", 0))  # 2
    print(Solution().characterReplacement("AABABBA", 2))  # 7
