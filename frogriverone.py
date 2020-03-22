# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
	zero_l = [0]*X
	t_sum = (X * (X+1))/2
	sum = 0
	
	for pos, val in enumerate(A):
		if val <= X and zero_l[val-1] == 0:
			sum += val
			zero_l[val-1] = 1
		if t_sum == sum:
			return pos
			
	return -1