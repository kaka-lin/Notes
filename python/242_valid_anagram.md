# 242. Valid Anagram

#### Discription

Given two strings s and t , write a function to determine if t is an [anagram](https://en.wikipedia.org/wiki/Anagram) of s.

#### Example:

```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

## Solution: Hash Table

- Runtime: 48 ms (84.31%)
- Memory Usage: 13.5 MB

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        length = len(s)
        table = {}
    
        for i in range(length):
            if s[i] in table:
                table[s[i]] += 1
            else:
                table[s[i]] = 1

            if t[i] in table:
                table[t[i]] -= 1
            else:
                table[t[i]] = -1
        
        for key, val in table.items():
            if val != 0:
                return False
                     
        return True
```

### Time complexity

- O(n)

### Space complexity

