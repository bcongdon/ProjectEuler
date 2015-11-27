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

def rotate_digits(num):
	string = num
	if len(string) <= 1:
		return num
	lastDigits = string[1:]
	firstDigit = string[:1]
	rotated = lastDigits + firstDigit
	return rotated

total = 0

for x in range(1,1000001):
	num = str(x)
	while True:
		if not isPrime(int(num)):
			break
		num = rotate_digits(num)
		#print num
		if int(num) == x:
			print "found: " + str(x)
			total += 1
			break
print "num circular primes: " + str(total)
