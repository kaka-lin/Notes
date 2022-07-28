# Recursion
def fibonacci(n: int) -> int:
    # base case
    if n < 2:
        return 1
    # recursive case
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    ans = fibonacci(35)
    print(ans)
