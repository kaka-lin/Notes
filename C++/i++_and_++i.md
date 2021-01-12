---
title: "[C++] i++ 與 ++i 的差別"
date: 2021-01-10
tags: [C++]
categories: [C++]
---

發現自己很容易搞混這兩個，於是簡單做個筆記記錄～

# i++ 與 ++i

- `i++`: `post-increment`

    ```
    在這一行程式完成之後，再進行+1的動作
    ```

- `++i`: `pre-increment`

    ```
    先進行+1，再進行後面的動作
    ```

## Example

```C
int x;
int y;

// Pre-increment
//   x is incremented by 1, then y is assigned the value of x
x = 1;
y = ++x; // x is now 2, y is also 2

// Post-increment
//   y is assigned the value of x, then x is incremented by 1
x = 1;
y = x++; // x is now 2, y is also 1

```
