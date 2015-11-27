_input = ""
with open('67.txt','r') as f:
	_input = f.read()


k = list()
for line in _input.split("\n"):
	lineList = list()
	for num in line.split(" "):
		lineList.append(int(num))
	k.append(lineList)
#k = list(reversed(k))

def recursive_row_sum(data, num):
	for i in range(len(data[num])):
		choice1 = data[num+1][i]
		choice2 = data[num+1][i+1]
		if choice1 > choice2:
			data[num][i] += choice1
		else:
			data[num][i] += choice2
	if len(data[num]) == 1:
		return data[num][0]
	else:
		return recursive_row_sum(data,num-1)

total = recursive_row_sum(k, len(k) - 2)
print total
