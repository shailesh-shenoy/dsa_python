# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_validity(node, left, right):
            if not node:
                return True
            return (
                (left < node.val < right)
                and check_validity(node.left, left, node.val)
                and check_validity(node.right, node.val, right)
            )

        return check_validity(root, float("-inf"), float("inf"))
