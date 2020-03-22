def solution(A):
    # write your code in Python 3.6
    l = 0
    N = len(A)
        
    for j in range(N):
        for i in range(N):
            if A[i] + i >= j - A[j]:
                l += 1
    
    l = l - int(N*(N+1)/2)
    
    return l