# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        nodes = {}

        old_dummy = Node(0)
        old_dummy.next = head
        new_dummy = Node(0)

        old = old_dummy
        new = new_dummy

        while old:
            nxt = old.next
            if not nxt:
                new.next = None
                old = nxt
                continue
            new_nxt = Node(nxt.val)
            if not nxt.random:
                new_nxt.random = None
            else:
                new_nxt.random = nxt.random.val
            if not nodes.get(nxt.val, None):
                nodes[nxt.val] = new_nxt
            old = nxt
            new.next = new_nxt
            new = new_nxt

        new = new_dummy.next
        while new:
            r = new.random
            if r:
                new.random = nodes[r]
            new = new.next

        print(new_dummy.next)
        return new_dummy.next

    def copy_random_list_simplified(self, head: "Optional[Node]") -> "Optional[Node]":
        old_to_copy = {None: None}
        curr = head

        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]
