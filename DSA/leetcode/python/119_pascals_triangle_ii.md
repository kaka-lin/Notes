# 119. Pascal's Triangle II

#### Discription

Given a non-negative index k where `k ≤ 33`, return the $k^{th}$ index row of the Pascal's triangle.

Note that the row index starts from 0.

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
###### In Pascal's triangle, each number is the sum of the two numbers directly above it.

#### Example:

```
Input: 3
Output: [1,3,3,1]
```

## Solution: Dynamic Programming

- Runtime: 24 ms (96.54%)
- Memory Usage: 12.7 MB (100%)

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal_list = [1]

        for row in range(1, rowIndex + 1):
            # Previous row
            prev_pascal_list = pascal_list

            # Start th new row
            pascal_list = [1]
            for col in range(1, row):
                pascal_list.append(prev_pascal_list[col-1] + prev_pascal_list[col])
            pascal_list.append(1)

        return pascal_list
```

### Time complexity

- $O(numRows^2)$
 
### Space complexity

- $O(k)$
