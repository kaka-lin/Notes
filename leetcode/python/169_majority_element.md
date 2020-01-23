# 169. Majority Element

#### Discription

Given an array of size n, find the majority element. The majority element is the element that appears `more than ⌊ n/2 ⌋ times`.

You may assume that the array is non-empty and the majority element always exist in the array.

#### Example:

```
Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2
```

## Solution 1: HashMap

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        record = {}
        for num in nums:
            if num not in record:
                record[num] = 1
            else:
                record[num] += 1
        
        return max(record.items(), key=operator.itemgetter(1))[0]
```

### Time complexity

- O(n)

### Space complexity

- O(n)

## Solution 2: Sort

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
```

### Time complexity

- O(nlogn)

### Space complexity

- O(1) or O(n)

## Solution 3: [Boyer-Moore Voting Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)

- Runtime: ms (%)
- Memory Usage: MB (%)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
```

### Time complexity

- O(n)

### Space complexity

- O(1)
