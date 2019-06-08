from tree import TreeNode

"""Recursive Approach

Time complexity: O(N)

@Runtime: 32ms (95.17%)
@Memory Usage: 13.3 MB (10.50%)
"""
def inorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
        
    ans = []
    return _inorderTraversal(root, ans)
    
def _inorderTraversal(node: TreeNode, ans: List[int]) -> List[int]:
    if node.left:
        _inorderTraversal(node.left, ans)
        
    ans.append(node.val)

    if node.right:
        _inorderTraversal(node.right, ans)
        
    return ans
