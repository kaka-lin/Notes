# 7. Reverse Integer

#### Discription

Given a 32-bit signed integer, reverse digits of an integer.

Assume that your function returns 0 when the reversed integer overflows.

#### Example:

```
Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
```

## Solution 1: String

- Runtime: 40ms (81.25%)
- Memory Usage: 13.4 MB (12.43%)

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        str_x = str(x)
        ans = ''

        if x > 0:
            for i in range(len(str_x)-1, -1, -1):
                ans += str_x[i]
        else:
            str_x = str_x[1:]
            ans += '-'
            ans += str_x[::-1]
    
        # 32bit: [-214748364, 2147483647]
        ans = int(ans)    
        return 0 if ans < -2147483648 or ans > 2147483647 else ans
```

## Solution 2: Pop and Push

Repeatedlly "pop" the last digit of x 
and "push" it to the back of the rev.

- Runtime: 36ms (91.37%)
- Memory Usage: 13.3 MB (26.14%)

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        rev = 0

        if x > 0:
            while (x):
                pop = x % 10
                x //= 10
                rev = rev * 10 + pop
        else:
            x = -1 * x
            while (x):
                pop = x % 10
                x //= 10
                rev = rev * 10 + pop
            rev = -1 * rev

        return 0 if rev < INT_MIN or rev > INT_MAX else rev
```


### Time complexity: 

- O(log(x))

### Space complexity

- O(1)
