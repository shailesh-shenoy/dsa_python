class TreeNode:
    def __init__(self, key: int, val: any):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, key: int = None, val: any = None):
        self.root = TreeNode(key, val) if key is not None else None

    def add(self, key: int, val):
        new_n = TreeNode(key, val)

        if self.root is None:
            self.root = new_n
            return

        curr = self.root

        while True:
            if new_n.key <= curr.key:
                if not curr.left:
                    curr.left = new_n
                    return
                curr = curr.left
                continue

            if not curr.right:
                curr.right = new_n
                return
            curr = curr.right

    def search(self, key: int) -> TreeNode | None:
        if not self.root:
            return None

        curr = self.root

        while curr:
            if curr.key == key:
                return curr

            if key < curr.key:
                curr = curr.left
                continue

            curr = curr.right

        return None

    def traversal(self, type: str = "inorder"):
        if type == "preorder":
            self.pre_order_traversal(self.root)
            return
        if type == "postorder":
            self.post_order_traversal(self.root)
            return
        self.in_order_traversal(self.root)

    def in_order_traversal(self, curr: TreeNode):
        if not curr:
            return

        self.in_order_traversal(curr.left)
        print(curr.val)
        self.in_order_traversal(curr.right)

    def pre_order_traversal(self, curr: TreeNode):
        if not curr:
            return
        print(curr.val)
        self.pre_order_traversal(curr.left)
        self.pre_order_traversal(curr.right)

    def post_order_traversal(self, curr: TreeNode):
        if not curr:
            return

        self.post_order_traversal(curr.left)
        self.post_order_traversal(curr.right)
        print(curr.val)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(5, "five")
    bst.add(3, "three")
    bst.add(7, "seven")
    bst.add(2, "two")
    bst.add(4, "four")
    bst.add(6, "six")
    bst.add(8, "eight")
    print("In order traversal")
    bst.traversal()
    print("preorder traversal")
    bst.traversal(type="preorder")
    print("postorder traversal")
    bst.traversal(type="postorder")
    print("Binary Search")

    print(bst.search(5).val)  # five
    print(bst.search(3).val)  # three
    print(bst.search(7).val)  # seven
    print(bst.search(2).val)  # two
    print(bst.search(4).val)  # four
    print(bst.search(6).val)  # six
    print(bst.search(8).val)  # eight
    print(bst.search(9))  # None
    print(bst.search(1))  # None
    print(bst.search(0))  # None
    print(bst.search(10))  # None
    print(bst.search(11))  # None
    print(bst.search(12))  # None
    print(bst.search(13))  # None
    print(bst.search(14))  # None
