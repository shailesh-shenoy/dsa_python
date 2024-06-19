"""
race a car
[r, a, c, e, c, a, r]

"""
from collections import deque


class Solution:
    def isPalindromeST(self, s: str) -> bool:
        stack = []
        queue = deque()
        s = s.lower()
        for c in s:
            if "a" <= c <= "z" or "0" <= c <= "9":
                stack.append(c)
                queue.append(c)
        
        while stack and queue:
            if stack.pop() != queue.popleft():
                return False
        
        return True
            
    def isPalindromeTP(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not self.isAlphaNumeric(s[l]):
                l += 1
                continue
            if not self.isAlphaNumeric(s[r]):
                r -= 1
                continue
            
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

    def isAlphaNumeric(self, c):
        return ("a" <= c <= "z" or "0" <= c <= "9")