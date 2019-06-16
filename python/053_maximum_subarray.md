# 53. Maximum Subarray

#### Discription

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#### Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

## Solution: Dynamic Programming

If sum[i-1] is negative, it will only make a smaller sum, so if sum[i-1] is negative, we let sum[i] is nums[i], and we add only if sum[i-1] is non-negative.

- Runtime: 40 ms (93.49%)
- Memory Usage: 14 MB (13.39%)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        length = len(nums)
        table = [0] * length
        table[0] = nums[0]
        _max = table[0]

        for i in range(1, length):
            if table[i-1] < 0:
                table[i] = nums[i]
            else:
                table[i] = table[i-1] + nums[i]

            if table[i] > _max:
                _max = table[i]

        return _max
```

### Time complexity

- O(n)

### Space complexity

- O(n)
