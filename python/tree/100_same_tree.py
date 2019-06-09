"""Recursion

Time complexity: O(N)

@Runtime: 36ms (86.76%)
@Memory Usage: 13.3 MB (17.64%)
"""
from tree import TreeNode
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
