
fractions = set()
d = 1
d_max = 12000
while d <= d_max:
	i = int(float(d)/3)
	#print(i,d)
	while float(i)/d < .5:
		val = float(i)/d
		if val > (1.0/3) and val < 0.5 and not val in fractions:
			fractions.add(float(i)/d)
		i+= 1
	d += 1
	print d

print "Solution to 73 is " + str(len(fractions))
