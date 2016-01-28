import math
import fractions
max_num = 1500000

triples = [0] * (max_num + 1)

result = 0
sq_limit = int(math.sqrt(max_num / 2))

for x in range(2, sq_limit):
	for y in range(1, x):
		if (x+y) % 2 == 1 and fractions.gcd(y,x) == 1:
			a = x**2 + y**2
			b = x**2 - y**2
			c = 2 * x * y
			p = a + b + c
			while p <= max_num:
				triples[p] += 1
				if triples[p] == 1:
					result += 1
				if triples[p] == 2:
					result -= 1
				p += a+b+c
print result