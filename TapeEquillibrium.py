# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    B = []
    sum = 0
        
    for x in A:
        sum += x
    
    for i in range(len(A)-1):
        sum = sum - 2*A[i]
        B.append(abs(sum))
        
    return min(B)
	