#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int numPaths(int x, int y){
	if((x==20) || (y==20)){
		return 1;
	}
	//cout << x << "," << y << endl;
	return numPaths(x+1, y) + numPaths(y, x+1);
}

int main()
{
	cout << numPaths(0,0) << endl;
}