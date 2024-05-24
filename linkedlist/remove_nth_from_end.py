# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            curr = curr.next
            sz += 1

        print(sz)
        prev = ListNode()
        prev.next = curr = head

        for i in range(sz - n):
            prev = prev.next
            curr = curr.next

        print(prev, curr)
        if prev.next == head:
            return head.next

        if not curr:
            prev.next = None
        else:
            prev.next = curr.next

        return head

    def remove_nth_from_end_1_pass(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        ptr = head

        for i in range(n):
            ptr = ptr.next

        while ptr:
            prev = prev.next
            ptr = ptr.next

        prev.next = prev.next.next
        return head
