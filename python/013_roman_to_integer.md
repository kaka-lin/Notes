# 13. Roman to Integer

#### Discription

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

IV            4
IX            9
XL            40
XC            90
CD            400
CM            900
```

#### Example:

```
Input: "III"
Output: 3

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Solution:

In special case, like "IV" is 4, "IX" is 9 or "CD" = 400, is all `roman[i] < roman[i+1]`.  

- Runtime: 24 ms (99.68%)
- Memory Usage: 11.6 MB (87.66%)

```python
lass Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        
        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i+1]]:
                ans += roman[s[i]]
            else:
                ans -=roman[s[i]]
        ans += roman[s[-1]]
        
        return ans
```

### Time complexity

### Space complexity
