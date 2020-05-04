# Bitonic Champion Problem

- Input: A `bitonic sequence` A[1], A[2], ..., A[n] for distinct positive integers.

- Output: the index $i$ with $1 {\leq} i {\leq} n$ such that

    $$A[i] = \max_{1 {\leq} j {\leq} n} A[j]$$

#### Bitonic sequence

```
The bitonic sequence means "increasing" before the champion and "decreasing" after the champion
```

Exmaple

```
3 7 9 17 35 28 21 18 6 4
```

## Bitonic Champion Problem Complexity

- Upper bound: $O(logn)$

- Lower bound: $\Omega(logn)$
