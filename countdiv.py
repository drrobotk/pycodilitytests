from math import ceil, floor

def solution(A, B, K):
    return floor(B/K) - ceil(A/K) + 1