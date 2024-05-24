# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while True:
            min_val = float("inf")
            min_p = None
            min_index = -1
            for i, p in enumerate(lists):
                if not p:
                    continue
                if p.val > min_val:
                    continue
                min_val = p.val
                min_p = p
                p = p.next
                min_index = i

            print(min_p)
            if not min_p:
                break

            curr.next = min_p
            lists[min_index] = lists[min_index].next
            curr = curr.next

        return dummy.next
