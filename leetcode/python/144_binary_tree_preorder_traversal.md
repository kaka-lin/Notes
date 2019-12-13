# 144. Binary Tree Preorder Traversal

#### Discription

Given a binary tree, return the `preorder` traversal of its nodes' values.

inorder:

```
root tree -> left tree -> right tree
``` 

#### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

## Solution 1: Recursive

- Runtime: 32 ms (92.42%)
- Memory Usage: 13.2 MB (52.73%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        array = []
        self.preorderHelper(root, array)
        return array

    def preorderHelper(self, root: TreeNode, array: List[int]):
        array.append(root.val)

        if root.left:
            self.preorderHelper(root.left, array)

        if root.right:
            self.preorderHelper(root.right, array)
```

### Time complexity: 

- O(n)

### Space complexity

- worst case: O(n)
- average case: O(logn)

## Solution 2: Iterating

- Runtime: 24 ms (99.77%)
- Memory Usage: 13.1 MB (75.32%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        array = []

        while root:
            array.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                root = root.left
            elif stack:
                root = stack.pop()
            else:
                break

        return array
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
