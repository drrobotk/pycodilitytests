# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    l = 0
    A = [0]
    B = []
        
    for i in range(2,len(str(bin(N)))):
        if int(str(bin(N)[i])) == 1:
            B.append(i)
            
    for i in range(len(B)-1):
        for j in range(B[i], B[i+1]):
            if int(str(bin(N)[j])) == 0:
                l += 1
        A.append(l)
        l = 0
            
            
    return max(A)