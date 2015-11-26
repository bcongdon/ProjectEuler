ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
thousand = 8

def length_of_num_word(num):
	length = 0
	one = num % 10
	ten = ((num % 100) - one) / 10
	hundred_place = ((num % 1000) - (ten * 10) - one) / 100

	if hundred_place != 0:
		length += ones[hundred_place] + hundred
		if ten != 0 or one != 0:
			length += len("and")
	if ten == 0 or ten == 1:
		length += ones[ten * 10 + one]
	else:
		length += tens[ten] + ones[one]
	return length

_sum = 0
for x in range(1,1000):
	print length_of_num_word(x)
	_sum += length_of_num_word(x)
_sum += ones[1] + thousand
print "Sum: " + str(_sum) 
