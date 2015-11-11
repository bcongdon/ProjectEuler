product = 2
for x in range(1000-1):
	product *= 2
sum = 0
string = str(product)
for c in range(len(string)):
	sum += int(string[c])
print sum