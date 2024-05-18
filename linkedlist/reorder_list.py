# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        r = slow.next
        prev = slow.next = None
        while r:
            temp = r.next
            r.next = prev
            prev = r
            r = temp

        r = prev

        l = head
        while r:
            nxt = l.next
            r_nxt = r.next
            l.next = r
            r.next = nxt
            l = nxt
            r = r_nxt


if __name__ == "__main__":
    s = Solution()

    # 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    s.reorderList(head)

    # 1 -> 5 -> 2 -> 4 -> 3
    while head is not None:
        print(head.val)
        head = head.next
