import itertools

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


def validChain(chain):
	return all(isPrime(int(str(a[0])+str(a[1]))) for a in itertools.permutations(chain,2))

primes = list()
for x in range(10000):
	if isPrime(x):
		primes.append(x)

def find_chain():
	for a in primes:
		for b in primes[primes.index(a):]:
			if validChain([a,b]):
				for c in primes[primes.index(b):]:
					if validChain([a,b,c]):
						for d in primes[primes.index(c):]:
							if validChain([a,b,c,d]):
								for e in primes[primes.index(d):]:
									if validChain([a,b,c,d,e]):
										print (a,b,c,d,e)
										print sum([a,b,c,d,e])
										return
find_chain()