# 100. Same Tree 

#### Discription

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

#### Example 1:

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

#### Example 2:

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

#### Example 3:

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

## Solution 1: Recursion

- Runtime: 36ms (86.76%)
- Memory Usage: 13.3 MB (17.64%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
    
        if p is None or q is None:
            return False
    
        if p.val != q.val:
            return False
    
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
