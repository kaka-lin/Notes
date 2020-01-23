# 24. Swap Nodes in Pairs 

#### Discription

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

#### Example:

```
Given 1->2->3->4, you should return the list as 2->1->4->3.
```

## Solution: Iteratively

- Runtime: 24 ms (90.17%)
- Memory Usage: 12.8 MB (100%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:        
        dummy = ListNode(None)
        dummy.next = head
        root = dummy

        while root.next and root.next.next:
            prev, post = root.next, root.next.next
            prev.next = post.next
            post.next = prev
            root.next = post
            root = root.next.next
            
        return dummy.next
```

### Time complexity

- O(n)

### Space complexity

- O(1)
