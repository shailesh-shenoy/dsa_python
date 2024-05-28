# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        count = 1

        def dfs(curr):
            nonlocal count
            nonlocal res
            if not curr:
                return
            dfs(curr.left)
            if count == k:
                res = curr.val
            count += 1
            dfs(curr.right)

        dfs(root)
        return res

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        sorted = []
        curr = root
        stack = []
        count = 1
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if count == k:
                break
            count += 1
            curr = curr.right

        return curr.val


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(20)
    root.left.left.right = TreeNode(4)

    k = 8
    s = Solution()
    print(s.kthSmallest(root, k))
    print("Iterative")
    print(s.kthSmallestIterative(root, k))
