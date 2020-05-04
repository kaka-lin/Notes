# 53. Maximum Subarray

#### Discription

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#### Example:

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

## Solution 1: Divide and Conquer

Ref: [divide and conquer - maximum subarray](https://github.com/kaka-lin/Notes/tree/master/knowledge/recursion/02_divide_and_Conquer/maximum_subarray)

- Runtime: 124 ms (7.29%)
- Memory Usage: 13.6 MB (65.85%)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        k = len(nums) // 2
        left_sum = self.maxSubArray(nums[:k])
        right_sum = self.maxSubArray(nums[k:])
        middle_sum = self.maxCrossSubArray(nums[:k], nums[k:])

        return max(left_sum, right_sum, middle_sum)
    
    def maxCrossSubArray(self, left, right):
        
        left_sum = float("-inf")
        _sum = 0
        for index in range(len(left)-1, -1, -1):
            _sum += left[index]
            if _sum > left_sum:
                left_sum = _sum

        right_sum = float("-inf")
        _sum = 0
        for index in range(len(right)):
            _sum += right[index]
            if _sum > right_sum:
                right_sum = _sum
        
        return left_sum + right_sum
        
```

### Time complexity

- $O(nlogn)$

### Space complexity

- $O(nlogn)$

## Solution 2: Dynamic Programming

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

- $O(n)$

### Space complexity

- $O(n)$
