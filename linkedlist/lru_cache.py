class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        prev = None
        next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = {}
        self.start = Node(None, None)
        self.end = Node(None, None)
        self.start.next = self.end
        self.end.prev = self.start

    def get(self, key: int) -> int:
        if not self.data.get(key, None):
            return -1
        current = self.data[key]
        current.prev.next = current.next
        current.next.prev = current.prev
        end = self.end
        end.prev.next = current
        current.prev = end.prev
        current.next = end
        end.prev = current

        return current.val

    def put(self, key: int, value: int) -> None:
        start = self.start
        end = self.end
        if self.data.get(key, None):
            current = self.data[key]
            current.val = value
            current.prev.next = current.next
            current.next.prev = current.prev
            current.prev = end.prev
            end.prev.next = current
            end.prev = current
            current.next = end
            return

        self.size += 1
        current = Node(key, value)
        self.data[key] = current
        end.prev.next = current
        current.prev = end.prev
        current.next = end
        end.prev = current

        if self.size > self.capacity:
            current = start.next
            current.next.prev = start
            start.next = current.next
            self.data[current.key] = None
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
