import math
def sum_digits(n):
	_sum = 0
	while n:
		_sum += n % 10
		n /= 10
	return _sum
print sum_digits(math.factorial(100))
