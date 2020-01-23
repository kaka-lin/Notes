# 226. Invert Binary Tree

#### Discription

Invert a binary tree.

#### Example:

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

## Solution 1: Recursion

- Runtime: 24 ms (87.55%)
- Memory Usage: 12.7 MB (100%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Iterative

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        
        while stack:
            curr = stack.pop(0)
            if curr:
                temp = curr.left
                curr.left = curr.right
                curr.right = temp

                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                
        return root
```

### Time complexity

- O(n)

### Space complexity

- O(n)
