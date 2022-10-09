def max_heapity(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and data[child] < data[child+1]:
            child += 1

        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break


def build_max_heap(arr):
    n = len(arr)
    for start in range(n // 2 - 1, -1, -1):
        max_heapity(arr, start, n-1)


if __name__ == "__main__":
    data = [38, 14, 57, 59, 52, 19]
    print("Original:", data)
    build_max_heap(data)
    print("Max-Heap:", data) # [59, 52, 57, 14, 38, 19]

    print()
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    build_max_heap(data)
    print("Max-Heap:", data) # [42, 36, 26, 31, 33, 12, 7, 15, 23, 9]
