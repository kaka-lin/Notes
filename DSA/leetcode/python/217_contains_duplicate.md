# 217. Contains Duplicate

#### Discription

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

#### Example:

```
Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```

## Solution 1: Hash Table

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        array = set()
        
        for num in nums:
            if num in array:
                return True
            array.add(num)
        
        return False
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Pythonic

- Runtime: 108 ms (99.88%)
- Memory Usage: 18.1 MB (88.68%)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

### Time complexity

- O(n)

### Space complexity

- O(n)
