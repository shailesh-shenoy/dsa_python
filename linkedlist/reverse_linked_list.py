from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head
        prev = None

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    def reverseListRecursive(
        self, head: Optional[ListNode], prev: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None:
            return prev

        temp = head.next
        head.next = prev
        prev = head
        head = temp
        return self.reverseListRecursive(head, prev)


if __name__ == "__main__":
    s = Solution()

    # 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # 5 -> 4 -> 3 -> 2 -> 1
    result = s.reverseListRecursive(head, None)
    while result is not None:
        print(result.val)
        result = result.next
