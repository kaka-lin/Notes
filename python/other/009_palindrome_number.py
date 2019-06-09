"""Pop and Push

Repeatedlly "pop" the last digit of x 
and "push" it to the back of the rev.

@Runtime: 56ms (99.03%)
@Memory Usage: 13.2 MB (76.11%)
"""
def isPalindrome(x: int) -> bool:
    if x == 0:
        return True
    if x < 0 or x % 10 == 0:
        return False
    
    temp = x
    rev = 0
    while (temp):
        rev = rev * 10 + temp % 10
        temp //= 10
    
    return True if x == rev else False
