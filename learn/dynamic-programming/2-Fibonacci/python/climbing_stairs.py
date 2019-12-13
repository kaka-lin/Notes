# Dynamic programming
# Bottom-up
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    
    table = [0] * (n+1)
    table[1] = 1
    table[2] = 2
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]
        
    return table[n]

if __name__ == "__main__":
    ans = climbStairs(35)
    print(ans)
