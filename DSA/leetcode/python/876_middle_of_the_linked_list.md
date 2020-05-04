# 876. Middle of the Linked List

#### Discription

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

##### Note:

- The number of nodes in the given list will be between 1 and 100.

#### Example:

```
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
```

## Solution 1: Output to Array

- Runtime: 28ms (97.95%)
- Memory Usage: 13.1MB (75.48%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        table = []

        while head:
            table.append(head)
            head = head.next

        return table[(len(table) // 2)]
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Fast and Slow Pointer

Ref: https://www.youtube.com/watch?v=UitXxwVeOrk
