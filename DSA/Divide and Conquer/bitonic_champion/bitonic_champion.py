def bitonic_champion(nums, i, j):
    if i == j:
        return i

    k = (i+j) // 2
    if nums[k] > nums[k + 1]:
        return bitonic_champion(nums, i, k)
    else:
        return bitonic_champion(nums, k + 1, j)


if __name__ == "__main__":
    test = [3, 7, 9, 17, 28, 35, 21, 18, 6, 4]
    print("original:", test)
    print("Champion index: ", bitonic_champion(test, 0, len(test)) + 1)
