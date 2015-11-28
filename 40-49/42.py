from math import sqrt
contents = ""

def word_sum(word):
	value = 0
	for char in list(word):
		value += ord(char) - 64
	return value

def isTriangular(num):
	check = (8*num) + 1
	if sqrt(check) % 1 == 0:
		return True
	return False

with open("42-words.txt","r") as f:
	contents = f.read()

contents = contents.split(",")
parsed_contents = list()
for word in contents:
	parsed_contents.append(word.strip("\""))

total = 0

for word in parsed_contents:
	if isTriangular(word_sum(word)):
		print word
		total += 1

print "Total number of triangle words: " + str(total)