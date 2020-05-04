# 94. Binary Tree Inorder Traversal

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

- Runtime: 32 ms (91.99%)
- Memory Usage: 13.2 MB (56.18%)

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
        self._inorderTraversal(root, ans)
        return ans

    def _inorderTraversal(self, node: TreeNode, ans: List[int]):
        if node.left:
            self._inorderTraversal(node.left, ans)

        ans.append(node.val)

        if node.right:
            self._inorderTraversal(node.right, ans)
```

### Time complexity: 

- O(n)

### Space complexity

- worst case: O(n)
- average case: O(logn)

## Solution 2: Iterating

- Runtime: 32 ms (91.99%)
- Memory Usage: 13.1 MB (62.12%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        array = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            array.append(root.val)
            root = root.right

        return array
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
