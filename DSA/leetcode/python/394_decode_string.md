# 394. Decode String

#### Discription

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like `3a` or `2[4]`.


#### Example:

```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

## Solution:

- Runtime: 20ms (99.06%)
- Memory Usage: 12.7MB (100%)

```python
class Solution:
    def decodeString(self, s: str) -> str:
        pre_string = []
        repeat_stack = []
        tmp_string = ""
        tmp_repeat = ""
        ans = ""
        balance = 0
        
        for char in s:
            if (ord(char) - 48 < 10):
                tmp_repeat += char
            elif (char == "["):
                balance += 1
                repeat_stack.append(int(tmp_repeat))
                pre_string.append(tmp_string)
                tmp_repeat = ""
                tmp_string = ""
            elif (char == "]"):
                balance -=1
                if balance != 0:
                    tmp_string = pre_string.pop() + tmp_string * repeat_stack.pop()
                else:
                    ans = ans + pre_string.pop() + tmp_string * repeat_stack.pop()
                    tmp_string = ""
            else:
                tmp_string += char
            
        ans += tmp_string
        return ans
```

### Time complexity

- O(n)

### Space complexity

- O(n)
