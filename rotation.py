# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    k = 0
    # write your code in Python 3.6
    if len(A) != 0:
        for i in range(K):
            k = A[len(A)-1]
            A.pop()
            A.insert(0,k)
        
    return A

if __name__ == '__main__':
    A = []
    K = 3
    result = solution(A, K)
    print(result)