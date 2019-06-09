# 1. Binary Tree Inorder Traversal

#### Discription

Given a binary tree, return the `inorder` traversal of its nodes' values.

inorder:

```
left tree -> root tree -> right tree
``` 

#### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

## Solution 1: Recursive

- Runtime: 32ms (95.17%)
- Memory Usage: 13.3 MB (10.50%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        ans = []
        return self._inorderTraversal(root, ans)
    
    def _inorderTraversal(self, node: TreeNode, ans: List[int]) -> List[int]:
        if node.left:
            self._inorderTraversal(node.left, ans)
        
        ans.append(node.val)

        if node.right:
            self._inorderTraversal(node.right, ans)
        
        return ans
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
