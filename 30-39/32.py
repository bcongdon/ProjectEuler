products = list()

def isPandigital(string):
	numDigits = len(string)
	if numDigits >= 10:
		return False
	for i in range(1,numDigits + 1):
		if not str(i) in string:
			return False
	return True

def pandigitalProduct(a, b):
	c = a*b
	return isPandigital(str(a) + str(b) + str(c))

for x in range(0,10000):
	for y in range(0,10000):
		if len(str(x*y) + str(x) + str(y)) > 9:
			break
		if len(str(x*y) + str(x) + str(y)) != 9:
			continue
		if pandigitalProduct(x,y) and not x*y in products:
			print x*y
			products.append(x*y)

print sum(products)