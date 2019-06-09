# 160. Intersection of Two Linked Lists

#### Discription

Write a program to find the node at which the intersection of two singly linked lists begins.

#### Example:

## Solution 1: Two Pointers

- Runtime: 192ms (91.82%)
- Memory Usage: 41.8 MB (67.17%)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        
        ptr_a = headA
        ptr_b = headB
        
        while ptr_a is not ptr_b:
            ptr_a = headB if ptr_a is None else ptr_a.next
            ptr_b = headA if ptr_b is None else ptr_b.next
            
        return ptr_a
```

### Time complexity: 

- O(m+n)

### Space complexity

- O(1)
