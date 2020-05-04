# 1. Two Sum 

#### Discription

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

#### Example:

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution 1: One-pass Hash Table

- Runtime: 36ms (95.30%)
- Memory Usage: 14.1 MB (56.68%)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_dict = {}
        for i in range(len(nums)):
            find_value = target - nums[i]
            if find_value in value_dict:
                return [value_dict[find_value], i]
            value_dict[nums[i]] = i
```

### Time complexity: 

- O(n)

### Space complexity

- O(n)
