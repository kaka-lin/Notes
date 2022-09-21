# 二元搜尋樹 (Binary Search Tree) 介紹

`二元搜尋樹 (Binary Search Tree, BST)` 就是將資料按造大小來建立樹，規則為:

- 若它的左子樹不為空，則左子樹上所有節點的值均小於它的根節點的值
- 若它的右子樹不為空，則右子樹上所有節點的值均大於它的根節點的值；
- 它的左、右子樹也分別為二元搜尋樹

如下所示:

```
    4
   / \
  2   6
 / \ / \
1  3 5  7
```

## Search time

這邊來看一下 BST 的搜尋時間，如下:

```python
def search_bst(root, target):
    if target < root.val:
        return search_bst(root.left, target)
    elif target > root.val:
        return search_bst(root.right, target)
    else:
        return root.val
```

- worst case: O(n)

## Types of Binary Search Tree

| # | arbitrary BST | Red-Blue Tree | AVL Tree | Completed BST |
| :-: | :-: | :-: | :-: | :-: |
| worst search time | O(n) | O(log n) | O(log n) | O(log n) |
| maintenance after insertion | O(1) | O(1) | O(1) | O(n) |

```sh
restriction   loose   ------------------------------>  strict
                                                    (ordered array)
            arbitrary BST  Red-Blue Tree  AVL Tree   Completed BST

worst
search          O(n)     >   O(log n)   ≈  O(log n)  > O(log n)
time

maintenance
after           O(1)     <    O(1)      ≈    O(1)    <   O(n)
insertion
```

### Complete Binary Search Tree (Complete BST)

如果要維持 Complete 的性質:

> 需要花力氣去調整 node 位置

- insertion: O(n)

    如下所示:

    ```
       2               3
     /   \    =>     /   \
    1     3         2     4
                   /
                  1

    2 | 1 |3  =>  3 | 2 | 4 | 1

    Time Complexity: O(n)
    ```
