# 371. Sum of Two Integers

#### Discription

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

#### Example:

```
Input: a = 1, b = 2
Output: 3

Input: a = -2, b = 3
Output: 1
```

## Solution 1: Bit manipulation

Ref: https://www.youtube.com/watch?v=qq64FrA2UXQ

### Explain 

key point

```
2 -> 10
3 -> 11
```

explain with `1 + 3`:

``` 
   11 => this is called carry
1: 001 
3: 011
   ---
4: 100   

if we use "AND(&)":
   111 -> carry
    111
    111
    ---
    111 -> we can find carry

if we use "xor(^)":
   1 
    1010
    1100
    -----
    0110 -> "simulating addition"
```

#### Conclusion:

1. Find carries (&)
2. Do the "addition (^)
3. left-shifted carry (<<)

---

- Runtime: 32ms (93.36%)
- Memory Usage: 13.3 MB (14.29%)

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == -b:
            return 0
    
        if abs(a) > abs(b):
            a, b = b, a
        if a < 0:
            return -self.getSum(-a, -b)
    
        while b:
            carry = a & b
            a = a ^ b
            b = carry << 1
    
        return a
```

## Solution 2: Two’s Complement of negative

Ref: https://notfalse.net/20/signed-number-representations#2-Two8217s-Complement

### Explain

```
8bit: -128~127 => 254 = -2

    val = 254 -> 11111110
    val ^ 0ff -> 11111111
                 --------
                 00000001 -> 1, ~1 = -2
```

---

- Runtime: 28ms (98.50%)
- Memory Usage: 13.3 MB (13.55%)

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32bit: -2147483648 ~ 2147483647
        MAX = 0x7FFFFFFF # 2147483647
        mask = 0xFFFFFFFF

        while b:
            carry = a & b
            a = (a ^ b) & mask      # 確保為32bit
            b = (carry << 1) & mask # 確保為32bit

        # 如果a是負數，需做修正
        return a if a <= MAX else ~(a ^ mask)
```
