# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Return true if there is a path from root to target.
def DFS(root: TreeNode, target: TreeNode):
    stack = [root]
    visited = set(root)

    while stack:
        cur = stack.pop()
        if cur == target:
            return True

        if root.right and root.right not in visited:
            stack.append(root.right)

        if root.left and root.left not in visited:
            stack.append(root.left)

    return False
