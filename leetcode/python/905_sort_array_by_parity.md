# 905. Sort Array By Parity

#### Discription

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

#### Example:

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

#### Note:

1. 1 <= A.length <= 5000
2. 0 <= A[i] <= 5000

## Solution 1: Two Pass

- Runtime: 76 ms (91.65%)
- Memory Usage: 13.4 MB (98.70%)

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []

        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        return even + odd
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Sort

- Runtime: 72 ms (98.05%)
- Memory Usage: 13.3 MB (98.70%)

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key = lambda x: x % 2)
        return A
```

### Time complexity

- O(nlogn)

### Space complexity

- O(n)
