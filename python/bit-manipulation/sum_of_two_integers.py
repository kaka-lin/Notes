"""Bit manipulation

Ref: https://www.youtube.com/watch?v=qq64FrA2UXQ

key point: 2 (10), 3(11)
explain, 1 + 3:
     
       11 => this is called carry
    1: 001 
    3: 011
       ---
    4: 100   

    if we use "AND(&)":
       111 -> carry
        111
        111
        ---
        111 -> we can find carry

    if we use "xor(^)":
       1 
        1010
        1100
       -----
        0110 -> "simulating addition"

Conclusion:
    1. Find carries (&)
    2. Do the "addition (^)
    3. left-shifted carry (<<)

@Runtime: 32ms (93.36%)
@Memory Usage: 13.3 MB (14.29%)
"""

def getSum(a: int, b: int) -> int:
    if a == -b:
        return 0
    
    if abs(a) > abs(b):
        a, b = b, a
    if a < 0:
        return -getSum(-a, -b)
    
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    
    return a
