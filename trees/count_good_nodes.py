# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_stack = [root.val]
        good = 0

        def dfs(curr):
            m = max_stack[-1]
            nonlocal good
            if curr.val >= m:
                m = curr.val
                good += 1
            max_stack.append(m)
            if curr.left:
                dfs(curr.left)
                max_stack.pop()
            if curr.right:
                dfs(curr.right)
                max_stack.pop()

        dfs(root)
        return good

    def goodNodesOptimized(self, root: TreeNode) -> int:
        good = 0

        def dfs(curr, max_val):
            if not curr:
                return
            nonlocal good
            if curr.val >= max_val:
                good += 1
                max_val = curr.val
            dfs(curr.left, max_val)
            dfs(curr.right, max_val)

        dfs(root, root.val)
        return good
