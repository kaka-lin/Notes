import random


def quick_sort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        quick_sort(nums, lo, p - 1)
        quick_sort(nums, p + 1, hi)
    return nums


def partition(nums, lo, hi):
    # Choose random pivot
    index = random.randint(0, len(nums) - 1)
    nums[index], nums[hi] = nums[hi], nums[index]
    pivot = nums[hi]

    # 遍歷陣列，將小於等於 pivot 的元素和 i 位置的元素交換
    i = lo
    for j in range(lo, hi):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    # 將 pivot 和與第 i 個元素交換: 就切成兩半邊
    nums[i], nums[hi] = nums[hi], nums[i]
    return i


if __name__ == "__main__":
    data = [1, 5, 3, 2, 8, 7, 6, 4]
    print("original:", data)
    print("Sorted:", quick_sort(data, 0, len(data) - 1))
