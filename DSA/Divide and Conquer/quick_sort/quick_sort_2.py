def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    lt = [n for n in nums if n < pivot]
    gt = [n for n in nums if n > pivot]
    eq = [n for n in nums if n == pivot]
    return quick_sort(lt)+eq+quick_sort(gt)


if __name__ == "__main__":
    test = [1, 5, 3, 2, 8, 7, 6, 4]
    print("original:", test)
    print("Sorted:", quick_sort(test))
