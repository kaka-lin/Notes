import math


def bubble_sort(data):
    # loop to access each array element
    for i in range(len(data)):
        # loop to compare array elements
        for j in range(0, len(data) - i - 1):
            # compare two adjacent elements
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def bubble_sort_2(data):
    n = len(data)
    while n > 1:
        n -= 1
        for i in range(n):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
    return data


if __name__ == "__main__":
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    print("Sorted:", bubble_sort(data)) # [7, 9, 12, 15, 23, 26, 31, 33, 36, 42]

    data = [40, 30, 60, 50, 20]
    print("original:", data)
    print("Sorted:", bubble_sort_2(data)) # [20, 30, 40, 50, 60]
