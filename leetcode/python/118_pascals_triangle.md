# 118. Pascal's Triangle

#### Discription

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
###### In Pascal's triangle, each number is the sum of the two numbers directly above it.

#### Example:

```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## Solution: Dynamic Programming

- Runtime: 20 ms (98.97%)
- Memory Usage: 12.7 MB (100%)

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_list = []
        for row in range(numRows):
            pascal_list.append([0] * (row+1))
            for col in range(len(pascal_list[row])):
                self.helper(row, col, pascal_list)
        
        return pascal_list
            
    def helper(self, nr, nc, pascal_list):
        if nc == 0 or nc == nr:
            pascal_list[nr][nc] = 1
        else:
            pascal_list[nr][nc] = pascal_list[nr - 1][nc - 1] \
                                + pascal_list[nr - 1][nc]
            
```

### Time complexity

- $O(numRows^2)$
 
### Space complexity

- $O(numRows^2)$
