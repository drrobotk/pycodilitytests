# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_end = max_slice = A[0]
    n = len(A)
    
    for i in range(1,n):
        max_end = max(A[i], max_end + A[i])
        max_slice = max(max_slice, max_end)
    
    return max_slice