# 733. Flood Fill

#### Discription

An `image` is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate `(sr, sc)` representing the starting pixel (row and column) of the flood fill, and a pixel value `newColor`, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

#### Example:

```
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
```

## Solution:

- Runtime: 68 ms (99.54%)
- Memory Usage: 12.6 MB (100%)

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = []
        visited = []
        originColor = image[sr][sc]
        image[sr][sc] = newColor
        queue.append((sr, sc))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c = queue.pop(0)
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != originColor:
                    continue
                else:
                    if (x, y) not in visited:
                        queue.append((x, y))
                        visited.append((x, y))
                        image[x][y] = newColor

        return image
```

### Time complexity

- O(N)

### Space complexity

- O(N)
