# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        level = 0
        max_level = -1

        def dfs(curr):
            nonlocal level
            nonlocal max_level
            if not curr:
                return
            if level > max_level:
                result.append(curr.val)
                max_level = level

            if curr.right:
                level += 1
                dfs(curr.right)
                level -= 1
            level += 1
            dfs(curr.left)
            level -= 1

        dfs(root)
        return result

    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []

        q = deque([root])
        while q:
            rightmost = None
            for i in range(len(q)):
                curr = q.popleft()
                rightmost = curr
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(rightmost.val)

        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.left = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.left.right.left = TreeNode(8)
    root.left.left.left.right = TreeNode(9)
    s = Solution()
    print(s.rightSideView(root))
    print(s.rightSideViewBFS(root))
