from math import sqrt

def isPentagonal(num):
	check = sqrt(24*num + 1) + 1
	check /= 6
	if check.is_integer():
		return True
	return False

def isHexagonal(num):
	check = (sqrt(8*num +1) + 1)/4
	if check.is_integer():
		return True
	return False

currentTriangle = 40756
n = 285
foundMatch = False
while True:
	n+= 1
	currentTriangle = n*(n+1)/2
	if isPentagonal(currentTriangle) and isHexagonal(currentTriangle):
		print currentTriangle
		break
