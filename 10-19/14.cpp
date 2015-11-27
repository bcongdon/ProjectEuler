#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int chainSum(int startingNum){
	long current = startingNum;
	int count = 1;
	while(current > 1){
		count ++;
		//Even
		if(current%2 == 0){
			current = current / 2;
		}
		//Odd
		else{
			current = 3*current + 1;
		}
	}
	return count;
}

int main()
{
	int largestSum = 0;
	int longestIndex = 0;
	for(int i = 0; i < 1000000; i++){
		if(chainSum(i) > largestSum){
			largestSum = chainSum(i);
			longestIndex = i;
		}
	}
	cout << largestSum << endl;
	cout << longestIndex << endl;
}