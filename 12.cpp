#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int triangleNumber(int i){
	int output = 0;
	for(int j = 1; j < i; j++){
		output += j;
	}
	return output;
}

int numFactors(int i){
	int numDivisors = 1;
	for(int j = 1; j <= sqrt(i); j++){
		if(i%j == 0){
			numDivisors+=2;
		}
	}
	return numDivisors;
}

int main()
{
	int seriesIndex = 1;
	int curr = 0;
	int highestFactor = 0;
	cout << numFactors(28) << endl;
	bool found = false;
	while(!found){
		if(numFactors(curr) >= 500){
			found = true;
			cout << curr << endl;

		}
		else{
			seriesIndex ++;
			curr = triangleNumber(seriesIndex);
			if(numFactors(curr) > highestFactor){
				highestFactor = numFactors(curr);
				cout << highestFactor << endl;
			}
		}
	}
}