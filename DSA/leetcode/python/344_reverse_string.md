# 344. Reverse String

#### Discription

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by `modifying the input array in-place with O(1) extra memory`.

You may assume all the characters consist of [printable ascii characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

#### Example 1:

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

#### Example 2:

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solution 1: Two Pointers

- Runtime: 212 ms (70.29%)
- Memory Usage: 17.2 MB (100%)

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        prev, post = 0, len(s) - 1
        while prev < post:
            s[prev], s[post] = s[post], s[prev]
            prev, post = prev + 1, post - 1
```

### Time complexity

- O(N)

### Space complexity

- O(1)

## Solution 2: Pythonic

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
```
