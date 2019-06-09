"""Reversing a string

@Runtime: 40ms (81.25%)
@Memory Usage: 13.4 MB (12.43%)
"""
def reverse(x: int) -> int:
    if x == 0:
        return 0

    str_x = str(x)
    ans = ''

    if x > 0:
        for i in range(len(str_x)-1, -1, -1):
            ans += str_x[i]
    else:
        str_x = str_x[1:]
        ans += '-'
        ans += str_x[::-1]
    
    # 32bit: [-214748364, 2147483647]
    ans = int(ans)    
    return 0 if ans < -2147483648 or ans > 2147483647 else ans

"""Pop and Push

Repeatedlly "pop" the last digit of x 
and "push" it to the back of the rev.

@Runtime: 36ms (91.37%)
@Memory Usage: 13.3 MB (26.14%)
"""
def reverse2(x: int) -> int:
    if x == 0:
        return 0

    INT_MAX = 2147483647
    INT_MIN = -2147483648
    rev = 0

    if x > 0:
        while (x):
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
    else:
        x = -1 * x
        while (x):
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        rev = -1 * rev

    return 0 if rev < INT_MIN or rev > INT_MAX else rev
