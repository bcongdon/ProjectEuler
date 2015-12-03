import itertools

iterStr = '0123456789'
lexi_permutations = itertools.permutations(iterStr, len(iterStr))
lexi_permutations = list(lexi_permutations)

def toInt(arr):
	string = ""
	for x in arr:
		string += x
	return string

int_permutations = [toInt(x) for x in lexi_permutations]
print int_permutations[1000000-1]