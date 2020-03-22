# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    z = 0
    c = 0
    
    for x in A:
        if x == 0:
            z += 1
        else:
            c += z
            
    if c > 1000000000:
        return -1
    else:
        return c
