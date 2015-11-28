def sum_digits(num):
	digits = [int(i) for i in list(str(num))]
	return sum(digits)

max_sum = (0,0,0)
for a in range(1,100):
	for b in range(1,100):
		_sum = sum_digits(a**b)
		if _sum > max_sum[2]:
			max_sum = (a,b,_sum)
print max_sum