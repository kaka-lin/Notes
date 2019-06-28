# 102. Binary Tree Level Order Traversal

[Level-order Traversal - Introduction](https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/990/)

#### Discription

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#### Example:

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

## Solution:

- Runtime: 32 ms (99.58%)
- Memory Usage: 13.5 MB (33.61%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = [root]
        level_ans = []
        level_stack = []

        while root and stack:
            while stack:
                root = stack.pop(0)
                level_ans.append(root.val)

                if root.left:
                    level_stack.append(root.left)
                if root.right:
                    level_stack.append(root.right)
                    
            ans.append(level_ans)
            stack = level_stack
            level_ans = []
            level_stack = []
            
        return ans
```

### Time complexity

### Space complexity
