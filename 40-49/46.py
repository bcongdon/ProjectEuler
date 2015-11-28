from math import sqrt
def isPrime(num):
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

x = 1
while True:
	x+=1
	if isPrime(x):
		primes.append(x)
		continue
	if x % 2 == 0:
		continue
	matchFound = False
	for prime in primes:
		check = x - prime
		if sqrt(check / 2).is_integer():
			matchFound = True
	if matchFound == False:
		print x
		break
