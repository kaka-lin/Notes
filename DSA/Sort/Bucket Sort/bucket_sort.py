import math


def bucket_sort(nums):
    buckets = []

    # Create empty buckets
    for i in range(len(nums) + 1):
        buckets.append([])

    # Put list elements into different buckets based on the size (normalization)
    max_num, min_num = max(nums), min(nums)
    size = (max_num - min_num) / len(nums)
    for data in nums:
        idx = int((data - min_num) / size)
        buckets[idx].append(data)

    # Sort the elements of each bucket
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    # Get the sorted elements
    k = 0
    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            nums[k] = buckets[i][j]
            k += 1

    return nums


if __name__ == "__main__":
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    print("Sorted:", bucket_sort(data)) # [7, 9, 12, 15, 23, 26, 31, 33, 36, 42]
