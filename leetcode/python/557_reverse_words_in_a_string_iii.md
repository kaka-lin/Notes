# 557. Reverse Words in a String III

#### Discription

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

#### Example:

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

#### Note:

In the string, each word is separated by single space and there will not be any extra space in the string.

## Solution 1:

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        for sub_s in s.split(" "):
            ans += self.helper(sub_s)
            ans += " "
        
        return ans[:-1]
            
    def helper(self, sub_s: str) -> str:
        if not sub_s:
            return ""
        
        sub_ans = self.helper(sub_s[1:])
        return sub_ans + sub_s[0]
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Pythonic

- Runtime: 28 ms (85.62%)
- Memory Usage: 13.2 MB (96.15%)

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(x[::-1] for x in s.split())
```
