largest = 0
for x in range(0,1000000):
	temp = str(x) + str(2*x)
	if "0" not in temp:
		if len(set(temp)) == 9 and len(temp) == 9:
			if int(temp) > largest:
				largest = int(temp)
print largest