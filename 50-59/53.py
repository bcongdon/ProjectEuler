import math

def gen_string_of_len(x):
	string = ""
	for i in range(x):
		string += str(i)
	return string[:x]

def get_combinations(n,r):
	if r > n:
		return -1
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

total = 0
for n in range(1,101):
	for r in range(1,n+1):
		if get_combinations(n,r) > 1000000:
			total += 1

print total