def getDigits(num):
	string = str(num)
	arr = [int(i) for i in list(string)]
	arr.sort()
	return arr

x = 0
while True:
	x+= 1
	matchFound = True
	for i in range(2,7):
		if getDigits(x) != getDigits(i * x):
			matchFound = False
	if matchFound:
		print x
		break