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

        self.update = False # when inser/delete update array

    def __str__(self):
        if not self.inorder_array:
            self._inorder(self.root)

        return f"Default print (inorder):\n\t{str([i for i in self.inorder_array])}"

    @property
    def update(self):
        return self._update

    @update.setter
    def update(self, boolen):
        self._update = boolen
        if self.update:
            self.inorder_array = []
            self.preorder_array = []
            self.postorder_array = []
            self.update = False

    def insert(self, data):
        self.update = True
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.val:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(node.right, data)

    def printInorder(self):
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

    def printPreorder(self):
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

    def printPostorder(self):
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

    # 在給定的 BST 中找到最小值節點
    def findMinimum(self, root):
        while (root.left):
            root = root.left
        return root

    def delete(self, data):
        self.update = True
        self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node

        if data == node.val:
            if node.left == None:
                node = node.right
            elif node.right == None:
                node = node.left
            else:
                # deletion of nodes with 2 children
                # find the inorder successor and replace the current node
                # inorder successor: 為右子樹中的最小值
                min_node = self.findMinimum(node.right)
                node.val = min_node.val

                # ** key step ** recurse on node.right but with key = node.val (min val in right subtree)
                node.right = self._delete(node.right, node.val)
        elif data < node.val:
            node.left = self._delete(node.left, data)
        else:
            node.right = self._delete(node.right, data)

        return node

if __name__ == "__main__":
    input_1 = [4, 2, 6, 1, 3, 5, 7]
    #input_1 = [4, 2, 5, 6, 3, 7, 1, 8]
    #input_1 = [4, 2, 5, 1, 3, 6, 7, 8]
    print("input: {}".format(input_1))
    print("="*30)

    print(f"[Build Tree]")
    tree = BinarySearchTree()
    for i in input_1:
        tree.insert(i)
    print(tree)
    tree.printPreorder()
    tree.printInorder()
    tree.printPostorder()

    # Insert: 8
    print(f"[Insertion: 8]")
    tree.insert(8)
    print(tree)
    tree.printPreorder()
    tree.printInorder()
    tree.printPostorder()

    # Delete: 8
    print(f"[Deletion: 5]")
    tree.delete(5)
    print(tree)
    tree.printPreorder()
    tree.printInorder()
    tree.printPostorder()
    print("="*30)

    #########################################
    input_2 = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print("input: {}".format(input_2))
    print("="*30)

    print(f"[Build Tree]")
    tree = BinarySearchTree()
    for i in input_2:
        tree.insert(i)
    print(tree)
    tree.printPreorder()
    tree.printInorder()
    tree.printPostorder()

    # Delete: 8
    print(f"[Deletion: 3]")
    tree.delete(3)
    print(tree)
    tree.printPreorder()  # [8, 4, 1, 6, 7, 10, 14, 13]
    tree.printInorder()   # [1, 4, 6, 7, 8, 10, 13, 14]
    tree.printPostorder() # [1, 7, 6, 4, 13, 14, 10, 8]
