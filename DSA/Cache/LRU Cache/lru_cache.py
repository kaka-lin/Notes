# Class for a Doubly LinkedList Node
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# LRU cache class
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)  # dummy
        self.tail = Node(0, 0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def insertToHead(self, node: Node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def removeNode(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            value = node.value
            self.removeNode(node)
            self.insertToHead(node)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.removeNode(node)
            self.insertToHead(node)
        else:
            # handles if capacity is reached
            if self.count >= self.capacity:
                tail_node = self.tail.prev
                self.removeNode(tail_node)
                del self.map[tail_node.key]
                self.count -= 1

            node = Node(key, value)
            self.map[key] = node
            self.insertToHead(node)
            self.count += 1


if __name__ == "__main__":
    print('Going to test the LRU Cache Implementation')
    cache = LRUCache(2)

    # it will store a key (1) with value
    # 10 in the cache.
    cache.put(1, 10)

    # it will store a key (1) with value 10 in the cache.
    cache.put(2, 20)
    print('Value for the key: 1 is {}'.format(cache.get(1)))  # returns 10

    # evicts key 2 and store a key (3) with
    # value 30 in the cache.
    cache.put(3, 30)

    print('Value for the key: 2 is {}'.format(
        cache.get(2)))  # returns -1 (not found)

    # evicts key 1 and store a key (4) with
    # value 40 in the cache.
    cache.put(4, 40)
    print('Value for the key: 1 is {}'.format(
        cache.get(1)))  # returns -1 (not found)
    print('Value for the key: 3 is {}'.format(cache.get(3)))  # returns 30
    print('Value for the key: 4 is {}'.format(cache.get(4)))  # returns 40
