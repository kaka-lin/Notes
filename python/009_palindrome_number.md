# 9. Palindrome Number 

#### Discription

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Coud you solve it without converting the integer to a string?

#### Example:

```
Input: 121
Output: true

Input: -121
Output: false
Explanation: 121- != -121

Input: 10
Output: false
```

## Solution 1: Pop and Push

Repeatedlly "pop" the last digit of x 
and "push" it to the back of the rev.

- Runtime: 56ms (99.03%)
- Memory Usage: 13.2 MB (76.11%)

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
    
        temp = x
        rev = 0
        while (temp):
            rev = rev * 10 + temp % 10
            temp //= 10
    
        return True if x == rev else False
```

### Time complexity: 

- O(log(x))

### Space complexity

- O(1)
