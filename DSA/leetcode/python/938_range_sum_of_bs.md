# 938. Range Sum of BST 

#### Discription

Given the `root` node of a binary search tree, return the sum of values of all nodes with value between `L` and `R` (inclusive).

The binary search tree is guaranteed to have unique values.

#### Example:

```
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

## Solution: Depth First Search

- Runtime: 212 ms (93.81%)
- Memory Usage: 20.5 MB (100%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum_val = 0
        self.dfs(root, L, R)
        return self.sum_val

    def dfs(self, root, L, R):
        if root:
            if L <= root.val and root.val <=  R:
                self.sum_val += root.val

            if root.val > L:
                self.dfs(root.left, L, R)

            if root.val < R:
                self.dfs(root.right, L, R)
```

### Time complexity

- O(N), where N is the number of nodes in the tree.

### Space complexity

- O(H), where H is the height of the tree.
