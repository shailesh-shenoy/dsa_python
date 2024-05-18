from collections import defaultdict
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frq_t = defaultdict(int)
        frq_w = defaultdict(int)

        for c in t:
            frq_t[c] += 1

        def check_frq_equality():
            for k, v in frq_t.items():
                if v != frq_w[k]:
                    return False
            return True

        def contains_frq():
            for k, v in frq_t.items():
                if v > frq_w[k]:
                    return False
            return True

        l = 0
        min_l = 0
        min_r = 0
        min_w = math.inf
        for r, c in enumerate(s):
            frq_w[c] += 1

            if not contains_frq():
                continue
            while contains_frq() or check_frq_equality():
                c = s[l]
                frq_w[c] -= 1
                l += 1

            # l -= 1
            # frq_w[c] += 1
            # while check_frq_equality():
            #     c = s[l]
            #     frq_w[c] -= 1
            #     l += 1

            w = r - l + 2
            if w <= min_w:
                min_w = w
                min_l = l
                min_r = r

        if min_w == math.inf:
            return ""

        return s[min_l : min_r + 1]


if __name__ == "__main__":
    s = Solution()

    # Example 1
    print(s.minWindow("ADOBECODEBANC", "ABC") == "BANC")

    # Example 2
    print(s.minWindow("a", "a") == "a")

    # Example 3
    print(s.minWindow("a", "aa") == "")

    # Example 4
    print(s.minWindow("a", "b") == "")

    # Example 5
    print(s.minWindow("ab", "b") == "b")

    # More big examples
