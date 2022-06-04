# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Return the length of the shortest path
# between root and target node.
def BFS(root: TreeNode, target: TreeNode) -> int:
    queue = [] # store all nodes which are waiting to be processed
    visited = set() # store all the nodes that we've visited
    step = 0 # number of steps neeeded from root to current node
    # initialize
    queue.append((root, step))
    visited.add(root)

    while queue:
        # iterate the nodes which are already in the queue
        cur, step = queue.pop(0)
        if cur.val == target.val:
            return step

        if cur.left and cur.left not in visited:
            queue.append((cur.left, step + 1))
            visited.add(cur.left)

        if cur.right and cur.right not in visited:
            queue.append((cur.right, step + 1))
            visited.add(cur.right)

    return -1 # there is no path from root to target
