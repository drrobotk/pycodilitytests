# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    n = len(A)
    
    if n == 0:
        return -1
    
    c = sorted(A)[n//2]
    
    if A.count(c) > n/2:
        return A.index(c)
    else:
        return -1

