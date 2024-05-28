# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        result = [[root.val]]
        queue.append((root, 0))
        level = 1
        result = []
        while queue:
            curr = queue.popleft()
            node = curr[0]
            level = curr[1]
            if level > len(result) - 1:
                result.append([])
            result[level].append(node.val)
            level += 1
            if node.left:
                queue.append((node.left, level))
            if node.right:
                queue.append((node.right, level))

        return result

    def levelOrderAlt(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        result = []
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level)

        return result


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # Add more nodes to test
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(8)
    root.right.right.right = TreeNode(10)
    root.right.right.left = TreeNode(11)
    root.left.left.left = TreeNode(12)
    root.left.left.right = TreeNode(13)
    root.left.right.left = TreeNode(14)
    root.left.right.right = TreeNode(15)
    s = Solution()
    print(s.levelOrder(root))
    print(s.levelOrderAlt(root))
