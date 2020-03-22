def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        m = 0
    else:
        m = max(A)
        
    A = set(A)
    B = set(range(1, m+1))
    D = B - A
    
    if len(D) == 0:
        return m+1
    else:
        return min(D)