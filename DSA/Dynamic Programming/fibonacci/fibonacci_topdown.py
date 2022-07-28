# Dynamic programming
# Top-Down with Memoization
def fibonacci(n):
    table = {0: 1, 1: 1}
    for i in range(2, n+1):
        table[i] = 0
    return recur_fib(n, table)


def recur_fib(n, table):
    if table[n] > 0:
        return table[n]

    # save the result to aviod recomputation
    table[n] = recur_fib(n-1, table) + recur_fib(n-2, table)
    return table[n]


if __name__ == "__main__":
    ans = fibonacci(35)
    print(ans)


