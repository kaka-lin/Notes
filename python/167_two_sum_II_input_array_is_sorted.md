# 167. Two Sum II - Input array is sorted

#### Discription

Given an array of integers that is already `sorted in ascending` order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

##### Note:

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.

#### Example:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

## Solution:

- Runtime: 36ms (94.20%)
- Memory Usage: 13.5MB (76.45%)

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {}

        for i in range(len(numbers)):
            rest = target - numbers[i]
            if rest in table:
                return [table[rest], i + 1]
            else:
                table[numbers[i]] = i+1
```

### Time complexity

- O(n)

### Space complexity

- O(n)
