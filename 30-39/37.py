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

def truncate_one(num):
	check = num
	while check > 0:
		if not isPrime(check):
			return False
		string = str(check)[1:]
		if string == '':
			break
		check = int(str(check)[1:])
	return True

def truncate_two(num):
	check = num
	while check > 0:
		if not isPrime(check):
			return False
		string = str(check)
		if string[:len(string)-1] == '':
			break
		check = int(string[:len(string)-1])
	return True

#print "Building primes list."
for x in range(1000000):
	if isPrime(x):
		primes.append(x)
		#print x
	# if x % 100000 == 0:
	# 	print x / 1000000.0
#print "Found " + str(len(primes)) + " primes."

total = 0
i = 0
for prime in primes:
	if len(str(prime)) <= 1:
		continue
	# if i % 1000 == 0:
	# 	print float(i) / len(primes)
	# i += 1
	if truncate_one(prime) and truncate_two(prime):
		print prime
		total += prime

print "Sum of special primes: " + str(total)