def int_to_bin(num):
	return int(bin(num)[2:])

def isPalindrome(num):
	string = str(num)
	if len(string) == 1 or len(string) == 0:
		return True
	if string[0] == string[len(string) - 1]:
		return isPalindrome(string[1:len(string)-1])
	else:
		return False
total = 0
for x in range(1, 1000000):
	if isPalindrome(x) and isPalindrome(int_to_bin(x)):
		print "Found: " + str(x) + " (10), " + str(int_to_bin(x)) + " (2)"
		total += x

print "Sum: " + str(total)
