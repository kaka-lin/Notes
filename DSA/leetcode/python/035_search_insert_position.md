# 35. Search Insert Position

#### Discription

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

#### Example:

```
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 7
Output: 4
```

## Solution: Array

- Runtime: 32 ms (93.73%)
- Memory Usage: 13.4 MB (98.27%)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target == nums[i] or target < nums[i]:
                return i

        return len(nums)
```

### Time complexity

- O(n)

### Space complexity

## Solution: Binary Search

- Runtime: 28 ms (98.70%)
- Memory Usage: 13.5 MB (93.66%)

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low
```

### Time complexity

- O(logn)

### Space complexity
