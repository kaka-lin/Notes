# 145. Binary Tree Postorder Traversal

#### Discription

Given a binary tree, return the `postorder` traversal of its nodes' values.

inorder:

```
left tree -> rigth tree -> root tree
``` 

#### Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
```

## Solution 1: Recursive

- Runtime: 32 ms (91.82%)
- Memory Usage: 13 MB (95.36%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        array = []
        self.postorderHelper(root, array)
        return array

    def postorderHelper(self, root: TreeNode, array: List[int]):
        if root.left:
            self.postorderHelper(root.left, array)

        if root.right:
            self.postorderHelper(root.right, array)

        array.append(root.val)
```

### Time complexity: 

- O(n)

### Space complexity

- worst case: O(n)
- average case: O(logn)

## Solution 2: Iterating

- Runtime: 36 ms (75.55%)
- Memory Usage: 13.2 MB (37.93%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pre = None
        array = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.right and pre != root.right:
                stack.append(root)
                root = root.right
                continue

            array.append(root.val)
            pre = root
            root = None

        return array
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
