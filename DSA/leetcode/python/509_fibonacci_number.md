# 509. Fibonacci Number

#### Discription

![](https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/Figures/recursion/fibonacci.png)

#### Example 1:

```
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

#### Example 2:
```
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## Solution: Top-Down

- Runtime: 24 ms (95.55%)
- Memory Usage: 12.7 MB (100%)

```python
class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        
        cache = {0: 0, 1: 1}
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]
        
        return cache[N]
```

### Time complexity

- O(N)

### Space complexity

- O(N)
