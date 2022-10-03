import math


def max_heapity(arr, start, end):
    root = start
    while True:
        child = 2 * root + 1
        # 若子節點指標超出範圍則結束
        if child > end:
            break

        # 先比較左右兩個子節點大小，選擇最大的那個子節點
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1

        # 如果 root 的值小於 child 最大值，則交換 (符合 max-heap 的特性)
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break


def build_max_heap(arr):
    n = len(arr)
    for start in range(n // 2 - 1, -1, -1):
        max_heapity(arr, start, n-1)


def heap_sort(arr):
    # 首先將資料轉換為 heap 資料結構
    build_max_heap(arr)
    print("Max Heap:", arr)

    # 我們將第一個元素(root)和已經排好的元素前一位(unsorted part)做交換
    # 再重新調整 unsorted part 使其符合 max-heap 特性
    # 直到排序完畢。
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapity(arr, 0, i-1)


if __name__ == "__main__":
    data = [38, 14, 57, 59, 52, 19]
    print("Original:", data)
    heap_sort(data) # heap: [59, 52, 57, 14, 38, 19]
    print("Sorted:", data) # [14, 19, 38, 52, 57, 59]

    print()
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    heap_sort(data) # [42, 36, 26, 31, 33, 12, 7, 15, 23, 9]
    print("Sorted:", data) # [7, 9, 12, 15, 23, 26, 31, 33, 36, 42]
