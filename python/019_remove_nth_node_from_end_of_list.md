# 19. Remove Nth Node From End of List 

#### Discription

Given a linked list, remove the n-th node from the end of list and return its head.


#### Example:

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

## Solution:

1. Using `dummy head` to treat special case (like the node we want to delete is the head in the linked list).

2. Using a table to save `current node`:

    - we can know the length of the linked list
    - we can quickly to get the node that we want to delete and the previous node through an index.
    - we specify `prevous.next` as `delete.next` (delete: the node we want to delete)
    - we specify `delete.next` as `None`
    - return `dummy.next`

    ```
    Input: 1->2->3->4->5, n = 2

    dummy: None->1->2->3->4->5
    table: [
        [None,1,2,3,4,5],
        [1,2,3,4,5],
        [2,3,4,5],
        [3,4,5],
        [4,5],
        [5],
    ]

    previous: 3->4->5
    delete:   4->5
    previous.next = delete.next
    delete.next = None

    dummy: None->1->2->3->5 
    return dummy.next
    ```

- Runtime: 32 ms (97.69%)
- Memory Usage: 13.1 MB (75.86%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        table = []
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy

        while curr:
            table.append(curr)
            curr = curr.next
        
        prev = table[len(table) - n - 1]
        delete = table[len(table) - n]
        prev.next = delete.next
        delete.next = None

        return dummy.next
```

### Time complexity

- O(n)

### Space complexity

- O(n)
