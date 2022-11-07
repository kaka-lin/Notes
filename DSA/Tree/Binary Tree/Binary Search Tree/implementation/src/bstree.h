#ifndef BSTREE_H
#define BSTREE_H

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
  int data;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : data(x), left(NULL), right(NULL) {}
  TreeNode *insertBsTree(TreeNode *root, int data);

  // Traversal
  void preorder(TreeNode *root);
  void inorder(TreeNode *root);
  void postorder(TreeNode *root);

  // Reconstruct
  // pre: preorder
  // in:  inorder
  TreeNode *reconstruct(int n, char pre[], char in[]);
};

void print_bs_tree(TreeNode *root);

#endif  // BSTREE_H
