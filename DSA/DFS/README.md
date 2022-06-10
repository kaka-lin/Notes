# Depth-first Search (DFS)

`Depth-first search (BFS)` is an algorithm to `traverse/search` in a `tree/graph`

We can use DFS:

- `pre-order`, `in-order` and `post-order` traversal.

There is a common feature among these three traversal orders: `we never trace back unless we reach the deepest node`.

That is also the largest difference between DFS and BFS, `BFS never go deeper unless it has already visited all nodes at the current level`.

## DFS implenmentation

Typically, we implement DFS using `recursion`. Stack plays an important role in recursion.

- DFS with recursion
  - advantage: easier to implemen
  - disadvantage: if the depth of recursion is too high, you will suffer from stack overflow
- DFS without recursion

## DFS Template

Depth-First Search (DFS) can also be used to find the path from the root node to the target node

### Template I

#### Implicit stack: [Call stack](https://en.wikipedia.org/wiki/Call_stack)

- Python: [dfs_recursive.py](dfs_recursive.py)
- Java:

    ```java
    boolean DFS(Node cur, Node target, Set<Node> visited) {
        return true if cur is target;
        for (next : each neighbor of cur) {
            if (next is not in visited) {
                add next to visted;
                return true if DFS(next, target, visited) == true;
            }
        }
        return false;
    }
    ```

### Template II

#### Explicit stack: use `while` loop and `stack` to simulate the `system call stack`

The advantage of the recursion solution is that it is easier to implement. However, there is a huge disadvantage: `if the depth of recursion is too high, you will suffer from stack overflow`.

In that case, you might want to use BFS instead or `implement DFS using an explicit stack`.

- Python: [dfs_iterative.py](dfs_iterative.py)
- Java:

    ```java
    boolean DFS(int root, int target) {
        Set<Node> visited;
        Stack<Node> stack;
        add root to stack;
        while (stack is not empty) {
            Node cur = the top element in stack;
            remove the cur from the stack;
            return true if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in visited) {
                    add next to visited;
                    add next to stack;
                }
            }
        }
        return false;
    }
    ```
