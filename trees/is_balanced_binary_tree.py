# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: TreeNode) -> tuple[bool, int]:
            if not node:
                return (True, 0)
            l = height(node.left)
            r = height(node.right)
            balanced = l[0] and r[0] and (abs(l[1] - r[1]) <= 1)
            return (balanced, 1 + max(l[1], r[1]))

        return height(root)[0]


if __name__ == "__main__":
    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    print(solution.isBalanced(root))  # Expected output: True

    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    solution = Solution()
    print(solution.isBalanced(root))  # Expected output: False
