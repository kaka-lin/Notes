# Binary Search Tree - Implementation

Implemente the Binary Search Tree

## Key Features

C/C++:

- [x] insertion
- [x] traversal
- [x] reconstruct
- [ ] deletion

Python:

- [x] insertion
- [x] traversal
- [ ] reconstruct
- [x] deletion

## Usage

Example 1: Insertion

```sh
input: [4, 2, 6, 1, 3, 5, 7], insert 8

    4
   / \
  2   5
 / \   \
1   3   6
         \
          7
           \
            8

Preorder: [4, 2, 1, 3, 5, 6, 7, 8]
Inorder: [1, 2, 3, 4, 5, 6, 7, 8]
Postoder: [1, 3, 2, 8, 7, 6, 5, 4]
Level-order: [4, 2, 6, 1, 3, 5, 7]
```

Example 2: Deletion

```sh
input: [8, 3, 10, 1, 6, 14, 4, 7, 13], delete: 3

     8
   /   \
  3     10
 / \     \
1   6    14
   / \   /
  4   7 13

after delete:

     8
   /   \
  4    10
 / \     \
1   6    14
     \   /
      7 13

preorder:  [8, 4, 1, 6, 7, 10, 14, 13]
inorder:  [1, 4, 6, 7, 8, 10, 13, 14]
postorder:  [1, 7, 6, 4, 13, 14, 10, 8]
```

### C/C++

- Build

    ```sh
    $ ./cmake-build.sh
    ```

- Run

    ```sh
    $ cd build
    $ ./bstree
    ```

## Reference

- [【Python】Binary Search Tree (二元搜尋樹) 資料結構實作(1)](https://lovedrinkcafe.com/python-binary-search-tree-1/)
- [【Python】Binary Search Tree (二元搜尋樹) 資料結構實作(2)](https://lovedrinkcafe.com/python-binary-search-tree-2/)
- [在 BST 中查找給定鍵的有序後繼](https://www.techiedelight.com/zh-tw/find-inorder-successor-given-key-bst/)
- [How to delete a node from a Binary Search Tree in Python?](https://www.codespeedy.com/delete-a-node-from-a-binary-search-tree-in-python/)
