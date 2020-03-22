# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    m = A[0]*A[1]*A[-1]
    l = A[-1]*A[-2]*A[-3]
    
    return max(m, l)
