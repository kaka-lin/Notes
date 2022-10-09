import math


def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        # key: 現在要插入的元素
        key = data[i]
        j = i-1 # sorted part
        # 沒有超出範圍且遇到的值大於要插入的值，則往右移
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data


if __name__ == "__main__":
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    print("Sorted:", insertion_sort(data)) # [7, 9, 12, 15, 23, 26, 31, 33, 36, 42]
