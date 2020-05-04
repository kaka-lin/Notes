# 700. Search in a Binary Search Tree

#### Discription

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

#### Example:

```
Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
```

You should return this subtree:

```
      2     
     / \   
    1   3
```

## Solution:

- Runtime: 64 ms (98.54%)
- Memory Usage: 14.8 MB (100%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if val == root.val:
                return root
            elif val > root.val:
                root = root.right
            else:
                root = root.left
        
        return None
```

### Time complexity

- O(N)

### Space complexity

- O(1)
