# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.previous = None
    
    def add(self, data):
        node = ListNode(data)
        self.head = node
        self.head.next = self.previous
        self.previous = self.head
    
    def print_linked_list(self):
        node = self.head
        _linked_list = f"{node.val}"
        while (node.next):
            _linked_list += f" -> {node.next.val}"
            node = node.next
        print(_linked_list)

class SortedLinkedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        current = ListNode(data)
        if self.head is None:
            self.head = current
            return 
        
        last = None
        ptr = self.head
        while (ptr != None and ptr.val < data):
            last = ptr
            ptr = ptr.next
        if last is None:
            current.next = self.head
            self.head = current
            return
        else:
            current.next = last.next
            last.next = current
            return 
    
    def print_linked_list(self):
        node = self.head
        _linked_list = f"{node.val}"
        while (node.next):
            _linked_list += f" -> {node.next.val}"
            node = node.next
        print(_linked_list) 
       
if __name__ == "__main__":
    input_1 = [4, 6, 2, 9, 7]
    print("input: {}".format(input_1))
    print("="*30)

    linkde_list = LinkedList()
    for i in input_1:
        linkde_list.add(i)
    
    linkde_list.print_linked_list()
    print(f"Add: {5}")
    linkde_list.add(5)
    linkde_list.print_linked_list()

    print(f"========== Sorted =========")
    linkde_list = SortedLinkedList()
    for i in input_1:
        linkde_list.add(i)
    
    linkde_list.print_linked_list()
    print(f"Add: {5}")
    linkde_list.add(5)
    linkde_list.print_linked_list()
