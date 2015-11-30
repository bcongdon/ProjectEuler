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

primes = list()
for x in range(1000001):
	if isPrime(x):
		primes.append(x)

longest = 0
for s in range(len(primes)-1,0,-1):
	print s
	index = s
	cum_sum = primes[index]
	while index < len(primes) and cum_sum < 1000000:
		index += 1
		cum_sum += primes[index]
		if cum_sum in primes and index - s > longest:
			longest = index - s
			print "Prime: " + str(cum_sum) + ", Length of chain: " + str(index - s)