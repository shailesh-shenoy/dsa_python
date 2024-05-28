# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        node = TreeNode(root_val)
        divider = root_val
        i = 0
        while inorder[i] != root_val:
            divider = inorder[i]
            i += 1
        inorder_left = inorder[0:i] if i > 0 else []
        inorder_right = inorder[i + 1 :] if i + 1 != len(inorder) else []
        i = 0
        while preorder[i] != divider:
            i += 1

        left = preorder[1 : i + 1] if len(preorder) > 1 else []
        right = preorder[i + 1 :] if i + 1 != len(preorder) else []

        if left:
            node.left = self.buildTree(left, inorder_left)
        if right:
            node.right = self.buildTree(right, inorder_right)

        return node

    def buildTreeOpt(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val = preorder[0]
        node = TreeNode(root_val)
        divider = inorder.index(root_val)

        node.left = self.buildTreeOpt(preorder[1 : divider + 1], inorder[0:divider])
        node.right = self.buildTreeOpt(preorder[divider + 1 :], inorder[divider + 1 :])
        return node

    def in_order_traversal(self, curr: TreeNode):
        if not curr:
            return

        self.in_order_traversal(curr.left)
        print(curr.val)
        self.in_order_traversal(curr.right)


if __name__ == "__main__":
    # preorder = [5, 3, 2, 4, 7, 6, 8]
    # inorder = [2, 3, 4, 5, 6, 7, 8]
    preorder = [2]
    inorder = [2]
    s = Solution()
    root = s.buildTreeOpt(preorder, inorder)
    print(s.in_order_traversal(root))
