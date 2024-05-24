# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            nonlocal max_diameter
            max_diameter = max(max_diameter, l + r)
            return 1 + max(l, r)

        height(root)
        return max_diameter


if __name__ == "__main__":
    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    print(solution.diameterOfBinaryTree(root))  # Expected output: 3

    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    solution = Solution()
    print(solution.diameterOfBinaryTree(root))  # Expected output: 1
