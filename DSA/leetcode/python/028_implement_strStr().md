# 28. Implement strStr()

#### Discription

Implement `strStr()`.

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#### Example:

```
Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

### Clarification:

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

## Solution:

- Runtime: 28ms (98.83%)
- Memory Usage: 13.4MB (38.10%)

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
```

### Time complexity

### Space complexity
