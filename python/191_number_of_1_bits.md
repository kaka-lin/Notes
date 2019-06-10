# 191.  Number of 1 Bits

#### Discription

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)).

#### Example:

```
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
```

## Solution 1: Loop and Flip 

The solution is straight-forward. We check each of the
32 bits of the number. If the bit is 1, we add one to the number of 1-bits.

- Runtime: 8 ms (99.56%)
- Memory Usage: 11.8 MB (26.43%)

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = n & 1
        for i in range(31):
            if (n & (2 << i)):
                bits += 1
        
        return bits
```

### Time complexity

The run time depends on the number of bits in `n`. Because `n` in this piece of code is a 32-bit integer, the time complexity is 

- O(1)

### Space complexity

- O(1)
