# 002. Add Two Numbers

#### Discription

You are given two `non-empty` linked lists representing two non-negative integers. The digits are stored in `reverse order` and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#### Example:

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

## Solution: Elementary Math

Hint: 

```
In loop: we need let `ptr = ptr.ext`

carry:           1
Input: 2 -> 4 -> 3
       5 -> 6 -> 4
       7 -> 0 -> 8 -> 0 (ptr.next)

* So, we use dummy head:

carry:               1
Input:     2 -> 4 -> 3
           5 -> 6 -> 4
      0 -> 7 -> 0 -> 8 (ptr.next)
      |
  dummy head
=> return: dummy_head.next
```

- Runtime: 72 ms (95.40%)
- Memory Usage: 13.4 MB (11.28%)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        ptr = result
        carry = 0

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            _sum = a + b + carry
            carry = _sum // 10
            
            ptr.next = ListNode(_sum % 10)
            ptr = ptr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry:
            ptr.next = ListNode(carry)

        return result.next
```

### Time complexity

- O(max(m, n))

### Space complexity

- O(max(m, n)) 
