""" Top-down Merge Sort

Recursion

"""

from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    # bottom case: empty or list of  a single element.
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
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

if __name__ == "__main__":
    test = [1, 5, 3, 2, 8, 7, 6, 4]
    print("original:", test)
    print("Sorted:", merge_sort(test))
