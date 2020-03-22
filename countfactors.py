# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # write your code in Python 3.6
    l = 0
    p = math.sqrt(N)
    
    for i in range(1, int(p)+1):
        if (N % i == 0):
            l += 2 
    
    if math.floor(p) == math.ceil(p):
        l -= 1
        
    return l

