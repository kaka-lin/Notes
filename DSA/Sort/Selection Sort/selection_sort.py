import math


def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data


if __name__ == "__main__":
    data = [9, 15, 12, 23, 33, 26, 7, 31, 42, 36]
    print("original:", data)
    print("Sorted:", selection_sort(data)) # [7, 9, 12, 15, 23, 26, 31, 33, 36, 42]
