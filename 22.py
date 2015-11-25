contents = ""

def name_value(pos, name):
	value = 0
	for char in list(name):
		value += ord(char) - 64
	return value * (pos)

with open("names.txt","r") as f:
	contents = f.read()

contents = contents.split(",")
parsed_contents = list()
for name in contents:
	parsed_contents.append(name.strip("\""))
parsed_contents.sort()
sum_total = 0
for i,name in enumerate(parsed_contents):
	sum_total += name_value(i+1,name)

print sum_total
#print name_value(938,"COLIN")