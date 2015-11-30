from math import sqrt
from decimal import Decimal, getcontext
getcontext().prec = 102

def sum_digits(num):
	digits = [int(i) for i in list(str(num))]
	return sum(digits)

total = 0
for x in range(100):
	if sqrt(x) % 1 != 0:
		total += sum_digits(int(str(Decimal(x).sqrt()).replace('.','')[:100]))
print total
