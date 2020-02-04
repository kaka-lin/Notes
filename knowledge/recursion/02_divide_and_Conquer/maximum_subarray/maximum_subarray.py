def max_subarray(nums, i, j):
    if i == j:
        return (i, j, nums[i])
    
    k = (i + j) // 2
    # If the maximum subarray appears in left.
    (left_i, left_j, left_sum) = max_subarray(nums, i, k)
    # If the maximum subarray appears in right.
    (right_i, right_j, right_sum) = max_subarray(nums, k+1, j)
    # If the maximum subarray crosses the middle.
    (middle_i, middle_j, middle_sum) = max_cross_subarray(nums, i, k, j)

    if left_sum >= right_sum and left_sum >= middle_sum:
        return (left_i, left_j, left_sum)
    elif right_sum >= left_sum and right_sum >= middle_sum:
        return (right_i, right_j, right_sum)
    else:
        return (middle_i, middle_j, middle_sum)

def max_cross_subarray(nums, i, k, j):
    left_sum = float("-inf")
    _sum = 0
    for index in range(k, i-1, -1):
        _sum += nums[index]
        if _sum > left_sum:
            left_sum = _sum
            max_left = index
    
    right_sum = float("-inf")
    _sum = 0
    for index in range(k+1, j+1):
        _sum += nums[index]
        if _sum > right_sum:
            right_sum = _sum
            max_right = index
    
    return (max_left, max_right, left_sum + right_sum)

if __name__ == "__main__":
    #test = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # 6
    test = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4] # 6
    i, j, max_sum = max_subarray(test, 0, len(test) - 1)

    print("original:", test)
    print("Maximum Subarray: {}, sum: {}".format(test[i:j+1], max_sum))
