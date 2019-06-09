# 136. Single Number

#### Discription

Given a `non-empty` array of integers, every element appears `twice` except for one. 
Find that single one.

##### Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

#### Example:

```
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
```

## Solution 1: Lsit operation

- Runtime: 1160 ms (8.54%)
- Memory Usage: 14.9 MB (36.99%)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        
        record_list = []
        
        for i in range(len(nums)):
            if nums[i] not in record_list:
                record_list.append(nums[i])
            else:
                record_list.remove(nums[i])
                
        return record_list[0]
```

### Time complexity

- O(n^2)

### Space complexity

- O(n)

## Solution 2: Bit Manipulation

### Concept

- If we take XOR of zero and some bit, it will return that bit

    ```
    a xor 0 = a
    ```

- If we take XOR of two same bits, it will return 0

    ```
    a xor a = 0
    ```
- Commutativity and Associativity

    ```
    a xor b xor a = (a xor a) xor b = 0 xor b = b
    ```
---
- Runtime: 36 ms (97.49%)
- Memory Usage: 14.7 MB (69.52%)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a
```

### Time complexity

- O(n)

### Space complexity

- O(1)
