# 542. 01 Matrix

#### Discription

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

#### Example 1:

```
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

#### Example 2:

```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

## Solution:

- Runtime: 656 ms (82.67%)
- Memory Usage: 14.7 MB (100%)

```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    d = self.bfs(matrix, i, j)
                    matrix[i][j] = d
        
        return matrix
                
    def bfs(self, matrix, r, c):
        queue, visited = [], []
        depth = 0
        queue.append((r, c, depth))
        visited.append((r, c, depth))
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            r, c, dep = queue.pop(0)
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                                
                if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                    continue
                else:
                    if (x, y) not in visited:
                        if matrix[x][y] == 0:
                            return dep + 1
                        
                        queue.append((x, y, dep + 1))
                        visited.append((x, y, dep + 1))
```

### Time complexity

- O(row * column)

### Space complexity

- O(row * column)
