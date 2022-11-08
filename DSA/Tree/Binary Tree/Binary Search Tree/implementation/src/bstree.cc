#include "bstree.h"

TreeNode *TreeNode::insertBsTree(TreeNode *root, int data) {
  TreeNode *current;

  if (root == NULL) {
    current = (TreeNode *)malloc(sizeof(TreeNode));
    assert(current != NULL);
    current->data = data;
    current->left = NULL;
    current->right = NULL;
    return (current);
  }

  if (data < root->data)
    root->left = insertBsTree(root->left, data);
  else
    root->right = insertBsTree(root->right, data);

  return (root);
}

void TreeNode::preorder(TreeNode *root) {
  if (root == NULL) return;
  printf("%d ", root->data);
  preorder(root->left);
  preorder(root->right);
  return;
}

void TreeNode::inorder(TreeNode *root) {
  if (root == NULL) return;
  inorder(root->left);
  printf("%d ", root->data);
  inorder(root->right);
  return;
}

void TreeNode::postorder(TreeNode *root) {
  if (root == NULL) return;
  postorder(root->left);
  postorder(root->right);
  printf("%d ", root->data);
  return;
}

TreeNode *TreeNode::reconstruct(int n, char pre[], char in[]) {
  // 給定前序、中序決定二元樹形狀
  //   - 前序: 就可以知道二元樹的根為何
  //   - 中序: 知道 root 就可以透過中序找到左子樹及右子樹
  // Example:
  //   前序: A E，中序: CBDAE
  //   -> 由前序得知 root 為 A
  //   -> 由中序得知 左子樹為 CBD，右子樹為 E
  //      -> 前序 BCD，中序 CBD 重建左子樹
  //      -> 前序 E，中序 E 重建左子樹
  //           A
  //         B   E
  //       C  D

  TreeNode *current;
  int leftn;
  int rightn;

  if (n == 0) return NULL;

  leftn = strchr(in, pre[0]) - in;  // the lenght of left
  rightn = n - leftn - 1;           // the lenght of right
  current = (TreeNode *)malloc(sizeof(TreeNode));
  assert(current != NULL);
  current->data = pre[0];
  current->left = reconstruct(leftn, pre + 1, in);
  current->right = reconstruct(rightn, pre + 1 + leftn, in + leftn + 1);
  return (current);
}

void print_bs_tree(TreeNode *root) {
  if (root == NULL) return;

  print_bs_tree(root->left);
  printf("%d ", root->data);
  print_bs_tree(root->right);
}
