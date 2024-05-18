from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        frq_s1 = {}
        frq_w = {}

        for i, c in enumerate(s1):
            frq_s1[c] = frq_s1.get(c, 0) + 1

            c = s2[i]
            frq_w[c] = frq_w.get(c, 0) + 1

        def areDictsEqual():
            for k, v in frq_s1.items():
                if v != frq_w.get(k, 0):
                    return False
            return True

        if areDictsEqual():
            return True

        l = 0
        r = len(s1) - 1
        while r < len(s2) - 1:
            frq_w[s2[l]] -= 1
            l += 1
            r += 1
            frq_w[s2[r]] = frq_w.get(s2[r], 0) + 1
            if areDictsEqual():
                return True

        return False

    def checkInclusionOptimized(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        frq_s1 = defaultdict(int)
        frq_w = defaultdict(int)

        for i, c in enumerate(s1):
            frq_s1[c] += 1
            c = s2[i]
            frq_w[c] += 1

        matches = 0
        for i in range(26):
            c = chr(ord("a") + i)
            if frq_s1[c] == frq_w[c]:
                matches += 1

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if matches == 26:
                return True

            if r == len(s2) - 1:
                return False

            c = s2[l]
            l += 1
            frq_w[c] -= 1
            if frq_w[c] == frq_s1[c]:
                matches += 1
            if frq_w[c] == frq_s1[c] - 1:
                matches -= 1

            r += 1
            c = s2[r]
            frq_w[c] += 1
            if frq_w[c] == frq_s1[c]:
                matches += 1
            if frq_w[c] == frq_s1[c] + 1:
                matches -= 1

        return False


if __name__ == "__main__":
    print(Solution().checkInclusion("ab", "eidbaooo"))  # True
    print(Solution().checkInclusion("ab", "eidboaoo"))  # False

    print("Optimized")

    print(Solution().checkInclusionOptimized("ab", "eidbaooo"))  # True
    print(Solution().checkInclusionOptimized("ab", "eidboaoo"))  # False
