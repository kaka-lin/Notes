# Principle of Recursion

```
Recursion is an approach to solving problems using a function that calls itself as a subroutine.
```

The trick is that each time a recursive function calls itself, it `reduces the given problem into subproblems`. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion.

A recursive function should have the following properties so that it does not result in an infinite loop:

- A simple `base case` (or cases) — a terminating scenario that does not use recursion to produce an answer.

    ```
    終止條件
    ```

- A set of rules, also known as recurrence relation that reduces all other cases towards the base case.

    ```
    一些規則，讓問題朝向終止條件去
    ```
