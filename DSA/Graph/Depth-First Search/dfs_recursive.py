# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Return true if there is a path from root to target.
def DFS(root: TreeNode, target: TreeNode, visited: Set) -> int:
    if root == target:
        return True

    if root.left and root.left not in visited:
        visited.add(root.left)
        return DFS(root.left, target, visited)

    if root.right and root.right not in visited:
        visited.add(root.right)
        return DFS(root.right, target, visited)

    return False
