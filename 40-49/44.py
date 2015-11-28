from math import sqrt
import sys

def isPentagonal(num):
	check = sqrt(24*num + 1) + 1
	check /= 6
	if check.is_integer():
		return True
	return False

def genPent(n):
	return n*(3*n - 1)/2

for k in range(1,10000):
	kPent = genPent(k)
	for j in range(k,10000):
		jPent = genPent(j)
		#print (jPent, kPent)
		if isPentagonal(jPent - kPent) and isPentagonal(jPent + kPent):
			print (k, j)
			print abs(kPent - jPent)
			sys.exit(0)


