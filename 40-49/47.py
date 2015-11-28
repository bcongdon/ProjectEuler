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

def generatePrimesTo(num):
    primes = list()
    for i in range(1,num):
        if isPrime(i):
            primes.append(i)
    primes.sort()
    return primes

PRIMES = generatePrimesTo(100000)

def numPrimeDivisors(num):
    divisors = 0
    for f in PRIMES:
        if f > num / 2 + 1:
            break
        if num % f == 0:
            divisors += 1
    return divisors

x = 2*3*5*7
intsFound = list()
while True:
	if len(intsFound) >= 4:
		print intsFound
		break
	if numPrimeDivisors(x) == 4:
		intsFound.append(x)
	else:
		intsFound = list()
	if x % 1000 == 0:
		print x
	x+= 1