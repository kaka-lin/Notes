from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    """
    Sorts an array in the ascending order in O(n log n) time

    @param
        nums: a list of numbers
    @return: the sorted list
    """
    n = len(nums)
    qsort(nums, 0, n - 1)
    return nums


def qsort(nums, lo, hi):
    """
    Helper

    @param
        nums: the list to sort
        lo  : the index of the firts element in the list
        hi  : the index of the last element in the list
    @return : the sorted list
    """

    if lo < hi:
        p = partition(nums, lo, hi)
        qsort(nums, lo, p - 1)
        qsort(nums, p + 1, hi)


def partition(nums, lo, hi):
    """ Lomuto Partition Scheme

    Picks the last element hi as a pivot
    and returns the index of pivot value in the sorted array.
    """
    pivot = nums[hi]
    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[hi] = nums[hi], nums[i]
    return i


if __name__ == "__main__":
    test = [1, 5, 3, 2, 8, 7, 6, 4]
    print("original:", test)
    print("Sorted:", quick_sort(test))
