numbers = dict()

def d(x):
	s = 0
	for i in range(1,x):
		if x % i == 0 and x != i:
			s += i
	return s

for x in range(1,10001):
	numbers[str(x)] = d(x)
	#print x
output = list()
for x in range(1,10001):
	y = numbers[str(x)]
	if x < y and 1 <= y and  y <= 10000 and str(y) in numbers.keys() and numbers[str(y)] == x:
		print x, y
		output.append(x)
		output.append(y)
print sum(output)