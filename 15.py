import sys
sys.setrecursionlimit(100000)

def numPaths(x,y):
	if x==20 and y==20:
		return 1
	return numPaths(x+1,y) + numPaths(x,y+1)

print numPaths(0,0)
