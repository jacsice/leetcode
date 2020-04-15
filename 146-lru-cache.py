class LinkedNode(object):
    def __init__(self, key=None, val=None):
        self.pre = None
        self.next = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.ht = {}
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove_node(self, node):
        pre = node.pre
        pre.next = node.next
        node.next.pre = pre

    def remove_tail(self):
        if self.capacity > 0:
            if self.tail.pre.val:
                self.ht.pop(self.tail.pre.key)
            pre = self.tail.pre.pre
            pre.next = self.tail
            self.tail.pre = pre

    def move_to_head(self, node):
        head_next = self.head.next
        self.head.next = node
        node.next = head_next
        node.pre = self.head
        head_next.pre = node

    def get(self, key: int) -> int:
        if key not in self.ht:
            return -1
        node = self.ht.get(key)
        self.remove_node(node)
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.ht:
            node = LinkedNode(key, value)
            self.move_to_head(node)
            self.ht[key] = node
            if len(self.ht) > self.capacity:
                self.remove_tail()
        else:
            node = self.ht[key]
            self.remove_node(node)
            node.val = value
            self.move_to_head(node)

    def __repr__(self):
        s = ''
        node = self.head.next
        while node.next:
            s += str(node.val)
            node = node.next
        return s


if __name__ == '__main__':
    lru = LRUCache(1)
    lru.put(2, 1)
    print(lru)
    lru.get(2)
    print(lru)
    lru.put(3, 2)
    print(lru)
    lru.get(2)
    print(lru)
    lru.get(3)
    print(lru)


