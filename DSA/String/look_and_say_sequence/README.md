# Look-and-say sequence

`Look-and-say sequence (外觀數列)`，又被稱為 `Morris number sequence (莫里斯數列)`

其為第 n 項描述了第 n-1 項的*數字分布*。它以1開始，如下所示:

`
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, ...
`

```
1: 讀作「1個1」，即 11
11: 讀作「2個1」，即 21
21: 讀作「1個2、1個1」，即 1211
1211: 讀作「1個1、1個2、2個1」，即 111221
111221: 讀作「3個1、2個2、1個1」，即 312211
312211: ...
```

- Leetcode: [38. Count and Say](https://leetcode.com/problems/count-and-say/)

The detail of explain of solution please see as below.

```
思路與解法說明請看下面。
```

## Question

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

- `countAndSay(1) = "1"`
- `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Given a positive integer `n`, return the `nth` term of the `count-and-say sequence`.

##### Example 1:

```
Input: n = 1
Output: "1"
Explanation: This is the base case.
```

##### Example 2:

```
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
```

##### Constraints:

- `1 <= n <= 30`

## Solution

1. 因為第 n 個數列與第 n-1 個數列有關，所以我們使用一個表個來存。
2. 當數字有`連續重複一樣時要加在一起念`，如:
    - "111221": 3個1, 2個2, 1個1 -> "212211"

    所以這邊我們使用 while 迴圈來判斷數列中，是否有連續重複的數字

    Exameple:

    ```sh
    "111221", count = 1
     i
      i+1

    "111221", count = 2
      i
       i+1

    "111221", count = 3
       i
        i+1

    s[i] != s[i+1] => 退出迴圈。
    ```

    如下所示:

    ```python
    # 不超過邊界，且數字一樣
    while i+1 < len(s) and s[i] == s[i+1]:
        count += 1
        i += 1
    ```

完整程式碼如下所示:

```python
def countAndSay(n):
    seq_dict = {1: "1", 2: "11"}
    for idx in range(3, n+1):
        prev = seq_dict[idx-1]
        ans = ''
        j = 0
        # like BFS
        while j < len(prev):
            count = 1
            # Count the same of continuous number
            while j+1 < len(prev) and prev[j] == prev[j+1]:
                count += 1
                j += 1
            ans += str(count) + str(prev[j])
            j += 1
        seq_dict[idx] = ans

    return seq_dict[n]
```

## Reference

- [外觀數列](https://zh.wikipedia.org/zh-tw/%E5%A4%96%E8%A7%80%E6%95%B8%E5%88%97)
