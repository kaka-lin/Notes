# 206. Reverse Linked List

#### Discription

Reverse a singly linked list.

#### Example:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

## Solution:

ref: https://www.youtube.com/watch?v=MRe3UsRadKw&t=4s

- Runtime: 32 ms (99.15%)
- Memory Usage: 18.7 MB (21.78%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        ptr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
           
        return ptr
```

### Time complexity

### Space complexity
