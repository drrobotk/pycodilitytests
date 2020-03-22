# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    start = [0]*n
    end = [0]*n
    
    for i in reversed(range(n-1)):
        start[i] = max(0, start[i+1] + A[i])
    
    for i in range(1, n):
        end[i] = max(0, end[i-1] + A[i])
    
    maxDoubleSlice = 0
    
    for i in range(1, n-1):
        maxDoubleSlice = max(maxDoubleSlice, start[i+1] + end[i-1])
    
    return maxDoubleSlice