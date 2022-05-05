# Tree

- `Tree`

    Each node of the tree will have a root value and a list of references to other nodes which are called `child nodes`. From graph view, a tree can also be defined as `a directed acyclic graph` which has `N nodes` and` N-1 edges`.

- `Binary Tree`

    A binary tree is a tree data structure in which each node has `at most two children`, which are referred to as the left child and the right child.

## Traverse a Tree

### Pre-order Traversal

```
root -> left subtree -> right subtrer
```

### In-order Traversal

```
left subtree -> root -> right subtrer
```

Typically, for `binary search tree`, we can retrieve all the data in sorted order using in-order traversal.

### Post-order Traversal


```
left subtree -> right subtrer -> root
```

* It is worth noting that when you `delete nodes` in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself.

* Also, post-order is widely use in `mathematical expression`. It is easier to write a program to parse a post-order expression.

## Solve Tree Problems Recursively

Recursion is one of the most powerful and frequently used techniques for solving tree problems.

Typically, we can solve a tree problem recursively using a `top-down approach` or using a `bottom-up approach`.

### Top-down approach

"Top-down" means that in each recursive call, we will visit the node first to come up with some values, and pass these values to its children when calling the function recursively. So the `"top-down"` solution can be considered as a kind of `preorder traversal`.

```
從上往下訪問，訪問現在節點，得出某些值，
然後在遞迴函式時將這些值傳給子節點。
所以可以被認為是 preorder
```

To be specific, the recursive function top_down(root, params) works like this:

```
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
5. return the answer if needed                      // answer <-- left_ans, right_ans
```

### Bottom-up approach

`"Bottom-up"` is another recursive solution. In each recursive call, we will firstly call the function recursively for all the children nodes and then come up with the answer according to the returned values and the value of the current node itself. This process can be regarded as a kind of `postorder traversal`.

```
在每次遞迴時，都會先對所有子節點遞歸調用函數，
然後根據返回值和當前節點本身的值得出答案
所以可以看成是是 postorder
```

Typically, a "bottom-up" recursive function bottom_up(root) will be something like this:

```
1. return specific value for null node
2. left_ans = bottom_up(root.left)      // call function recursively for left child
3. right_ans = bottom_up(root.right)    // call function recursively for right child
4. return answers                       // answer <-- left_ans, right_ans, root.val
```

### For example: Maximum Depth

Given a binary tree, find its `maximum depth`.

Solution: [104. Maximum Depth of Binary Tree](https://github.com/kaka-lin/leetcode/blob/main/leetcode/00104_maximum-depth-of-binary-tree/104-maximum-depth-of-binary-tree.py)

#### 1. Top-down

*Preorder Traversal*

```
1. return if root is null
2. if root is a leaf node:
3.     answer = max(answer, depth)         // update the answer if needed
4. maximum_depth(root.left, depth + 1)     // call the function recursively for left child
5. maximum_depth(root.right, depth + 1)    // call the function recursively for right child
```

#### 2. Bottom-up

*Postorder Traversal*

```
1. return 0 if root is null                 // return 0 for null node
2. left_depth = maximum_depth(root.left)
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at rootr
```
