# 912. Sort an Array

- [Merge Sort](https://github.com/kaka-lin/Notes/tree/master/knowledge/recursion/02_divide_and_Conquer/merge_sort)

#### Discription

Given an array of integers `nums`, sort the array in ascending order.

#### Example:

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
```

#### Constraints

- 1 <= nums.length <= 50000
- -50000 <= nums[i] <= 50000

## Solution 1: Merge Sort (Top-down Approach (Recursion))

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if left:
            result += left
        if right:
            result += right
        
        return result
```

### Time complexity

### Space complexity

## Solution 2: Merge Sort (Bottom-up Approach (Iteratively)))

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        size = 1
        result = nums

        while size < length:
            for index in range(0, length, size * 2):
                left = result[index : index + size]
                right = result[index + size : index + size * 2]
                result[index : index + size * 2] = self.merge(left, right)

            size *= 2
    
        return result
    
    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if left:
            result += left
        if right:
            result += right
        
        return result
```

### Time complexity

### Space complexity
