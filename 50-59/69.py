def relitively_prime(a,b):
	for i in range(2,b+1):
		if a % i == 0 and a % b == 0:
			return False
	return True
	
counts = [0] * 1000001
for i in range(2,1000001):
	for j in range(2, i):
		if relitively_prime(i,j):
			counts[i] += 1