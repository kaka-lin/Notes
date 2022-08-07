# Longest Palindromic Substring

## Question

- Leetcode: [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)


Given a string `s`, return *the longest palindromic substring* in `s`

##### Example 1:

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

##### Example 2:

```
Input: s = "cbbd"
Output: "bb"
```

##### Constraints:

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Solution

### Method 1: Brute-Force (Time Limit Exceeded)

Pick all possible starting and ending positions for a substring,
and verify if it is a palindrome.

```
窮舉所有可能的 Substring，判斷其是否為回文
```

```python
def longestPalindrome(s):
    if not s: return ""

    n = len(s)
    left, right, longest = 0, 0, 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            if isPalindrome(substr):
                if len(substr) > longest:
                    left, right, longest = i, j, len(substr)
    return s[left:right]
```

其中判斷是否為回文的方法為:

```python
def isPalindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
```

- Time-Complexity: $O(n^3)$, `Time Limit Exceeded`

