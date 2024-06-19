class Node:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next    

class MinStack:

    def __init__(self):
        self.top = None
        self.min_top = None

    def push(self, val: int):
        new_node = Node(val=val)
        new_min = Node(val=val)
        if not self.top:
            self.top = new_node
            self.min_top = new_min
            return        
        new_node.next = self.top
        self.top = new_node 
        
        new_min.val = min(self.min_top.val, val)
        new_min.next = self.min_top
        self.min_top = new_min
        
    
    def pop(self) -> int:
        val = self.top.val
        self.top = self.top.next
        self.min_top = self.min_top.next
        return val
    
    
    def top(self) -> int:
        return self.top.val

    def getMin(self) -> int:
        return self.min_top.val
        
