def isAbundant(num):
	_sum = 0
	for x in range(1, num/2 + 1):
		if num % x == 0:
			_sum += x
	return _sum > num

abundant_numbers = set([x for x in range(1,28123) if isAbundant(x)])
print "Found Abundant Numbers"
def isAbundantSum(num):
	for a in abundant_numbers:
		if a > num:
			return False
		if (num - a) in abundant_numbers:
			return True
	return False

print sum([x for x in range(1,28123) if not isAbundantSum(x)])