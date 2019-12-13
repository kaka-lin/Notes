# 27. Remove Element 

#### Discription

Given an array nums and a value val, remove all instances of that value `in-place` and return the new length.

Do not allocate extra space for another array, you must do this by `modifying the input array in-place` with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#### Example 1:

```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
```

#### Example 2:

```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.

```

## Solution 1: Two Pointes - when elements to remove are rare

Remove 

- Runtime: 32 ms (96.43%)
- Memory Usage: 13.2 MB (35.57%)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        length = len(nums)
        while (index < length):
            if nums[index] == val:
                nums.pop(index)
                length -= 1
            else:
                index += 1

        return length
```

### Time complexity

- O(n)

### Space complexity

- O(1)


## Solution 2: Two Pointes - Reorder

Reorder

- Runtime: 32 ms (96.43%)
- Memory Usage: 13.2 MB (35.57%)

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count
```

### Time complexity

- O(n)

### Space complexity

- O(1)
