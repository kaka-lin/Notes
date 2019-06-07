from typing import List

"""One-pass Hash Table

@Runtime: 36ms (95.30%)
@Memory Usage: 14.1 MB (56.68%)
"""
def twoSum(nums: List[int], target: int) -> List[int]:
    value_dict = {}
    for i in range(len(nums)):
        find_value = target - nums[i]
        if find_value in value_dict:
            return [value_dict[find_value], i]
        value_dict[nums[i]] = i
