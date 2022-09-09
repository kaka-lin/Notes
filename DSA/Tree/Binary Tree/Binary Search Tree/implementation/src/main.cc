#include <iostream>

#include "bstree.h"

int main() {
  TreeNode *root = NULL;
  // int insert_keys[8];

  // 4 2 5 6 3 7 1 8
  // for (int i = 0; i < 8; i++)
  //   scanf("%d", &(insert_keys[i]));
  int insert_keys[8] = {4, 2, 5, 6, 3, 7, 1, 8};


  for (int i = 0; i < 8; i++)
    root = root->insertBsTree(root, insert_keys[i]);
  //print_bs_tree(root);

  printf("preorder\n");
  root->preorder(root);
  printf("inorder\n");
  root->inorder(root);
  printf("postorder\n");
  root->postorder(root);

  // Reconstruct
  int length;
  // char preorder[80];
  // char inorder[80];
  TreeNode *root2;

  // pre: ABCED
  // in:  CBDAE
  // scanf("%s", preorder);
  // scanf("%s", inorder);
  char preorder[] = "ABCDE";
  char inorder[] = "CBDAE";
  length = strlen(preorder);
  assert(length = strlen(inorder));
  root2 = root2->reconstruct(length, preorder, inorder);
  root2->postorder(root2); // CDBEA (67,68,66,69,65)
  printf("\n");

  return 0;
}
