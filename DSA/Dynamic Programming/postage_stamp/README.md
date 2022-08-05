# Postage Stamp Problem

```
花越少的郵票，Cover 郵資
```

- Input:the postage n and the stamps with value v1, v2, ..., vk

    ![](images/stamp.png)

- Output: the `minimum` number of stamps to cover the postage

## Recursive Algorithms

The optimal solution $s_n$ can be recursively defined as:

$$ 1 + min_i(S_{n-v_i})$$

#### Example:

假設共有 4 種郵資: [3, 5, 7, 12]，那麼可能的情況有

- 從 solution 中拿掉 3 的郵票，剩下 S(n-3) 的郵資
- 從 solution 中拿掉 5 的郵票，剩下 S(n-5) 的郵資
- 從 solution 中拿掉 7 的郵票，剩下 S(n-7) 的郵資
- 從 solution 中拿掉 12 的郵票，剩下 S(n-12) 的郵資

可得:

$$ 1 + min(S_{n-3}, S_{n-5}, S_{n-7}, S_{n-12})$$

### Naive Recursive Algorithm

```c
Stamp(v, n)
    r_min = ∞
    // base case
    if n == 0
        return 0
    // recursive case
    for i = 1 to k
        r[i] =  Stamp(v, n - v[i])
        if r[i] < r_min
            r_min = r[i]
    return r_min + 1
```

Time-Complexity: $T(n) = \theta(k^n)$

## Dynamic Programming

### Step 1: Characterize an OPT Solution

- Subproblems
  - `S(i)`: the min #stamps with postage `i`
  - Goal: `S(n)`
- Optimal substructure: suppose we known the optimal sokution to `S(i)`, there are k case:
  - Case 1: there is a stamp with v1 in OPT:

    從 solution 中拿掉一張郵資為 v1 的郵票，剩下的部份是 S(i-v[1]) 的最佳解
  - Case 2: there is a stamp with v2 in OPT:

    從 solution 中拿掉一張郵資為 v2 的郵票，剩下的部份是 S(i-v[2]) 的最佳解
  - Case k: there is a stamp with vk in OPT:

    從 solution 中拿掉一張郵資為 vk 的郵票，剩下的部份是 S(i-v[k]) 的最佳解

### Step 2: Recursively Define the Value of an OPT Solution

- Subproblems
  - `S(i)`: the min #stamps with postage `i`
  - Goal: `S(n)`
- Optimal substructure: suppose we known the optimal sokution to `S(i)`, there are k case:
  - Case 1: there is a stamp with v1 in OPT: $S_i = 1 + S_{i-v_1}$
  - Case 2: there is a stamp with v2 in OPT: $S_i = 1 + S_{i-v_2}$
  - Case k: there is a stamp with vk in OPT: $S_i = 1 + S_{i-v_k}$

### Step3: Compute Value of an OPT Solution

#### Bottom-up method: solve smaller subproblems first

```c
Stamp(v, n)
    S[0] = 0
    for i = 1 to n
        r_min = ∞
        for j = 1 to k
            if S[i - v[j]] < r_min
                r_min = 1 + S[i - v[j]]
        S[i] = r_min
    return S[n]
```

Time-Complexity: $T(n) = \theta(kn)$

### Step 4: Construct an OPT Solution by Backtracking

```c
Stamp(v, n)
    S[0] = 0
    for i = 1 to n
        r_min = ∞
        for j = 1 to k
            if S[i - v[j]] < r_min
                r_min = 1 + S[i - v[j]]
                B[i] = j // backtracking dor stamp with v[j]
        S[i] = r_min
    return S[n], B
```

Time-Complexity: $T(n) = \theta(kn)$

```c
Print-Stamp-Selecion(v, n)
    (S, B) = Stamp(v, n)
    while n > 0
    print B[n]
    n = n - v[B[n]]
```

Time-Complexity: $T(n) = \theta(n)$
