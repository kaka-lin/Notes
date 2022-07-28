# Dynamic programming
# Bottom-Up with Memoization
def fibonacci(n):
    table = {0: 1, 1: 1}
    for i in range(2, n+1):
        table[i] = table[i-1] +  table[i-2]
    return table[n]


if __name__ == "__main__":
    ans = fibonacci(35)
    print(ans)


