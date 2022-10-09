""" Bottom-up Merge Sort

Iteratively

"""
from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    length = len(nums)
    size = 1
    result = nums

    while size < length:
        for index in range(0, length, size * 2):
            left = result[index : index + size]
            right = result[index + size : index + size * 2]
            result[index : index + size * 2] = merge(left, right)

        size *= 2

    return result


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
