# Recursion

## Principle of Recursion

```
Recursion is an approach to solving problems using a function that calls itself as a subroutine.
```

The trick is that each time a recursive function calls itself, it `reduces the given problem into subproblems`. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion.

A recursive function should have the following properties so that it does not result in an infinite loop:

- A simple `base case` (or cases) — a terminating scenario that does not use recursion to produce an answer.

    ```
    終止條件
    ```

- A set of rules, also known as `recurrence relation` that reduces all other cases towards the base case.

    ```
    一些規則，讓問題朝向終止條件去
    ```

## Recursion Function

For a problem, if there exists a recursive solution, we can follow the guidelines below to implement it.

For instance, we define the problem as the function F(X) to implement, where X is the input of the function which also defines the scope of the problem.

Then, in the function F(X), we will:

1. Break the problem down into smaller scopes, such as ${x_0} \in X, {x_1} \in X, ..., {x_n} \in X$;

2. Call function F(x_0), F(x_1), ..., F(x_n) recursively to solve the subproblems of X;

3. Finally, process the results from the recursive function calls to solve the problem corresponding to X.

### Example
`
Given a linked list, `swap every two adjacent nodes` and return its head.

```
e.g. for a list 1-> 2 -> 3 -> 4,
return the head of list as 2 -> 1 -> 4 -> 3.
```

We define the function to implement as `swap(head)`, where the input parameter `head` refers to the head of a linked list. The function should return the `head` of the new linked list that has any adjacent nodes swapped.

Following the guidelines we lay out above, we can implement the function as follows:

1. First, we swap the first two nodes in the list, i.e. `head` and `head.next`;
2. Then, we call the function self as `swap(head.next.next)` to swap the rest of the list following the first two nodes.
3. Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.

#### Solution:

- [Python](https://github.com/kaka-lin/leetcode/blob/main/leetcode/00024_swap-nodes-in-pairs/24-swap-nodes-in-pairs.py)

## Recurrence Relation

A recurrence is an equation or inequality that descirbes a function in terms of its value on smaller inputs.

There are two important things that one needs to figure out before implementing a recursive function:

- `recurrence relation`:

  the relationship between the result of a problem and the result of its subproblems.

- `base case (bottom cases)`:

  the case where one can compute the answer directly without any further recursion calls.

  ```
  終止條件
  ```

  Sometimes, the base cases are also called `bottom cases`, since they are often the cases where the problem has been reduced to the minimal scale, i.e. the bottom, if we consider that dividing the problem into subproblems is in a `top-down` manner.

### Example

Let's look at a classic problem, [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)

![](images/Pascal's%20Triangle.png)

- `Recurrence Relation`

    Let's start with the recurrence relation within the Pascal's Triangle.

    First of all, we define a function `f(i, j)` which returns the number in the Pascal's Triangle in the `i-th` row and `j-th` column.

    We then can represent the `recurrence relation` with the following formula:

    ```
    f(i,j) = f(i−1,j−1) + f(i−1,j)
    ```

- `Base Case`

    As one can see, the leftmost and rightmost numbers of each row are the `base cases` in this problem, which are always equal to 1.

    As a result, we can define the `base case` as follows:

    ```
    f(i, j) = 1 where i = 1 or j = i
    ```

#### Solution:

- [Python](https://github.com/kaka-lin/leetcode/blob/main/leetcode/00118_pascals-triangle/118-pascals-triangle.py)

## Duplicate Calculation in Recursio

Recursion is often an intuitive and powerful way to implement an algorithm. However, it might bring some undesired penalty to the performance, e.g. duplicate calculations, if we do not use it wisely.

We will then propose a common technique called `memoization` that can be used to avoid this problem.

### Example

Let's look at a classic problem, [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)

If we define the function `F(n)` to represent the Fibonacci number at the index of `n`, then you can derive the following recurrence relation:

- `Recurrence Relation`

    ```
    F(n) = F(n - 1) + F(n - 2)
    ```

- `Base Case`

    ```
    F(0) = 1, F(1) = 1
    ```

Solution:

```python
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

We can found, in order to obtain the result for `F(4)`, we would need to calculate the number `F(2)` twice.

### Memoization

To `eliminate the duplicate calculation` in the above case, one of the ideas would be to `store the intermediate results in the cache` so that we could reuse them later without re-calculation.

This idea is also known as `memoization`, which is a technique that is frequently used together with recursion.

Back up to [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number), Back to Fibonacci number, we can solve this issue with memorization, as below:

```python
def fibonacci(n):
    cache = {}
    def recur_fib(n):
        if n in cache:
            return cache[n]

        if n < 2:
            result = n
        else:
            result = c

        cache[n] = result
        return result

    return recur_fib(n)
```

#### Solution:

- [Python](https://github.com/kaka-lin/leetcode/blob/main/leetcode/00509_fibonacci-number/509-fibonacci-number.py)

## Time Complexity - Recursion

Given a recursion algorithm, its `time complexity` *O(T)* is typically the product of `the number of recursion invocations` (denoted as *R*) and `the time complexity of calculation` (denoted as *O(s)*) that incurs along with each recursion call:

```
O(T) = R * O(s)
```

### Example

In the problem of `printReverse`:

```python
printReverse(str) = printReverse(str[1...n]) + print(str[0])
```

1. recursively invoked n times: n
2. print the leading character: O(1)

   ```
   O(printReverse) = n * O(1) = O(n).
   ```

Ref: [Time Complexity - Recursion](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/1669/)

## Space Complexity - Recursion

Ref: [Space Complexity - Recursion](https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/1671/)

## Tail Recursion

`Tail recursion` is a recursion where the recursive call is the final instruction in the recursion function. And there should be only `one` recursive call in the function.

```
Tail recursion can avoid extra space incurred.
```

首先執行計算,然後執行遞歸調用,將當前步驟的結果傳遞到下一個遞歸步驟。
這導致最後一個語句的形式為`(return (recursive-function params))` 。基本上任何給定遞歸步驟的返回值都與下一個遞歸調用的返回值相同。

Ref: [什麼是尾遞歸? (What is tail recursion?)](https://tw.coderbridge.com/discussions/b945143a4ed74799b06a96804bbc9e05)


### Example

We have already seen an example of tail recursion in the solution of [Reverse String](https://github.com/kaka-lin/leetcode/blob/main/leetcode/00344_reverse-string/344-reverse-string.py).

Here is another example:

```python
def sum_non_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    if len(ls) == 0:
        return 0

    # not a tail recursion because it does some computation after the recursive call returned.
    return ls[0] + sum_non_tail_recursion(ls[1:])


def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    def helper(ls, acc):
        if len(ls) == 0:
            return acc
        # this is a tail recursion because the final instruction is a recursive call.
        return helper(ls[1:], ls[0] + acc)

    return helper(ls, 0)
```
