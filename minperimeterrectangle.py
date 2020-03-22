

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(N):
    # write your code in Python 3.6
    p = math.sqrt(N)
    A = 0
    B = 0
    
    for i in reversed(range(1,int(p)+1)):
        if (N % i == 0):
            A = int(N/i)
            B = i
            break
    
    return 2*(A+B)

