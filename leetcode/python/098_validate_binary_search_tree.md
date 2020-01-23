# 98. Validate Binary Search Tree

#### Discription

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys `less than` the node's key.
- The right subtree of a node contains only nodes with keys `greater than` the node's key.
- Both the left and right subtrees must also be binary search trees.

#### Example 1:

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

#### Example 2:

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Solution 1: Recursion

- Runtime: 36 ms (95.54%)
- Memory Usage: 14.9 MB (100%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, root, min_val, max_val):
        if not root:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        return self.helper(root.left, min_val, root.val) and \
               self.helper(root.right, root.val, max_val)
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2:  Inorder traversal

- Runtime: 36 ms (95.54%)
- Memory Usage: 15 MB (100%)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float("-inf")
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        
        return True
```

### Time complexity

- O(n)

### Space complexity

- O(n)
