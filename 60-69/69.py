def isPrime(num):
	from math import sqrt
	if(num < 2):
		return False

	if num is 2:
		return True

	if(num % 2 == 0):
		return False

	for i in range(2,int(sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

primes = [x for x in range(200) if isPrime(x)]

upper_limit = 1000000
_max = 1
for prime in primes:
	if _max * prime > upper_limit:
		print _max
		break
	_max *= prime