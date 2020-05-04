# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.inorder_array = []
        self.preorder_array = []
        self.postorder_array = []
    
    def __str__(self):
        if not self.inorder_array:
            self._inorder(self.root)

        return str([i for i in self.inorder_array])

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return self
        else:
            self._add(self.root, data)
    
    def _add(self, node, data):
        if data < node.val:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._add(node.left, data)
        else:
            if node.right == None:
                node.right = TreeNode(data)
            else:
                self._add(node.right, data)
    
    def print_inorder(self):
        if self.root is None:
            return "inorder: {}".format(self.inorder_array)

        if not self.inorder_array:
            self._inorder(self.root)

        print("inorder: ", self.inorder_array)
    
    # left -> root -> right
    def _inorder(self, node):
        if node.left:
            self._inorder(node.left)

        self.inorder_array.append(node.val)

        if node.right:
            self._inorder(node.right)
    
    def print_preorder(self):
        if self.root is None:
            return "preorder: {}".format(self.preorder_array)

        if not self.preorder_array:
            self._preorder(self.root)

        print("preorder: ", self.preorder_array)
    
    # root -> left -> right
    def _preorder(self, node):
        self.preorder_array.append(node.val)

        if node.left:
            self._preorder(node.left)

        if node.right:
            self._preorder(node.right)
    
    def print_postorder(self):
        if self.root is None:
            return "postorder: {}".format(self.postorder_array)

        if not self.postorder_array:
            self._postorder(self.root)

        print("postorder: ", self.postorder_array)
    
    # left -> right -> root
    def _postorder(self, node):
        if node.left:
            self._postorder(node.left)

        if node.right:
            self._postorder(node.right)
        
        self.postorder_array.append(node.val)
        
    
if __name__ == "__main__":
    #input_1 = [4, 6, 2, 9, 5]
    input_1 = [1, 3, 2, 4, 6, 7, 5, 9]
    print("input: {}".format(input_1))
    print("="*30)

    tree = BinarySearchTree()
    for i in input_1:
        tree.add(i)

    print(tree)
    tree.print_inorder()
    tree.print_preorder()
    tree.print_postorder()
