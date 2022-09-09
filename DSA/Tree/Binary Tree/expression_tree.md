# Binary Expression Tree

Each internal node corresponds to the operator and each leaf node corresponds to the operand.

Example:

A expression tree for 3 * (5+7) would be:

```sh
      *
    /   \
   3     +
        / \
       5   7
```

```sh
prefix: (* 3 (+ 5 7)) -> mul(3, plus(5, 7))
infix: 3 * (5+7) -> 四則運算
postfix: 3 5 7 + * -> 電腦上實際想要執行運算的方式
```

## Reference

- [Wiki: Binary expression tree](https://en.wikipedia.org/wiki/Binary_expression_tree)
- [Expression Tree](https://www.geeksforgeeks.org/expression-tree/)
