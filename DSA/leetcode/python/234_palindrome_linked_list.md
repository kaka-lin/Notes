# 234. Palindrome Linked List 

#### Discription

Given a singly linked list, determine if it is a palindrome.

#### Example:

```
Input: 1->2
Output: false

Input: 1->2->2->1
Output: true
```

#### Follow up:

Could you do it in O(n) time and O(1) space?

## Solution:

1. Find the middle of the linked list.
2. Reverse the second half of the linked list.
3. Compare.

- Runtime: 76 ms (84.86%)
- Memory Usage: 23.6 MB (92.34%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        # find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the linked list
        reverse = None
        curr = slow
        while curr:
            _next = curr.next
            curr.next = reverse
            reverse = curr
            curr = _next

        # compare
        backward = reverse
        forward = head
        while backward:
            if forward.val != backward.val:
                return False
            forward = forward.next
            backward = backward.next

        return True
```

### Time complexity

### Space complexity
