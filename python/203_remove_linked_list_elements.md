# 203. Remove Linked List Elements

#### Discription

Remove all elements from a linked list of integers that have value val.

#### Example:

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

## Solution:

Using dummy node can convenience to treat the special case, like the `val` appear at `head of list` and `immediately after it`.

For example: 

```
Input: 1 -> 1 -> 1
Output: []
```

- Runtime: 72ms (90.70%)
- Memory Usage: 16.1MB (99.7%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
```

### Time complexity

- O(n)

### Space complexity

- O(1)
