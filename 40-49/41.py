from math import sqrt

primes = list()

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

def isPandigital(num):
	digits = len(str(num))
	string = str(num)
	if digits == 1 and num != 1:
		return False
	for i in range(1,digits+1):
		if not str(i) in string:
			return False
	return True

i = 7654321
while not (isPandigital(i) and isPrime(i)):
	i -= 1
print i