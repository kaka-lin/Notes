# Time complexity: O(2^n)
def hanoi(n, A, B, C):
    if n == 1: # base case
        print(A, '--->', C)
    else: # recursive case
        hanoi(n-1, A, C, B)
        hanoi(1, A, B, C) # or print(A, '--->', C)
        hanoi(n-1, B, A, C)


if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
