def isRightTriangle(a,p):
	if p*(p-2*a) % 2*(p-a) == 0:
		return True
	return False

solutions = [0] * 1010

for p in range(1,1001):
	for a in range(2,p):
		for b in range(2,p-a):
			c = p - a - b
			if c*c == a*a + b*b:
				solutions[p] += 1
				print (a,b,c,p)

print "Most solutions when p=" + str(solutions.index(max(solutions)))	