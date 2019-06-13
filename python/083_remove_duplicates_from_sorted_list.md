# 83. Remove Duplicates from Sorted List

#### Discription

Given a sorted linked list, delete all duplicates such that each element appear only once.

#### Example:

```
Input: 1->1->2->3->3
Output: 1->2->
```

## Solution:

- Runtime: 44 ms (93.15%)
- Memory Usage: 13.1 MB (67.00%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        ptr = head
        while ptr and ptr.next:
            if ptr.next.val == ptr.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
    
        return head
```

### Time complexity

- O(n)

### Space complexity

- O(1)
