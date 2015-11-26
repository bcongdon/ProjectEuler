import sys
def sum_fifth_power(x):
	sum_powers = 0
	while x > 0:
		n = x % 10
		sum_powers += n*n*n*n*n
		x /= 10
	return sum_powers
total = 0
for x in range(2,2**23):
	if x == sum_fifth_power(x):
		print x
		total += x

print "Total: " + str(total)