def merge_sort(nums):
    # Base case
    if len(nums) == 1:
        return nums
    # Recursive case
    ## 1. divide 
    mid = len(nums) // 2
    ## 2. Conquer
    prev_list = merge_sort(nums[:mid])
    post_list = merge_sort(nums[mid:])
    ## 3. Combine
    return merge(prev_list, post_list)

def merge(prev_list, post_list):
    result = []

    while prev_list and post_list:
        if prev_list[0] < post_list[0]:
            result.append(prev_list.pop(0))
        else:
            result.append(post_list.pop(0))
    
    if prev_list:
        result += prev_list
    if post_list:
        result += post_list
    
    return result

if __name__ == "__main__":
    test = [6, 3, 5, 1, 8, 7, 2, 4]
    print("original:", test)
    print("Sorted:", merge_sort(test))
