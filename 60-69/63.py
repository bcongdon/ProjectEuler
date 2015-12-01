def num_digits(num):
	digits = [int(i) for i in list(str(num))]
	return len(digits)
total = 0
for b in range(1,10):
	for e in range(1,100):
		num = b**e
		if num_digits(num) == e:
			print str(b) + "^" + str(e) + " = " + str(num)
			total += 1
print "Total special numbers: " + str(total)