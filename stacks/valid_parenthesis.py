class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
            if not stack:
                return False
            t = stack.pop()
            if c != self.getValidBracket(t):
                return False
        
        return len(stack) == 0
    
    def getValidBracket(self, t: str):
        if t == "(":
            return ")"
        if t == "[":
            return "]"
        if t == "{":
            return "}"
        return ""
                