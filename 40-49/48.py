series = 0
for i in range(1,1001):
	series += i**i
string = str(series)
print string[-10:]