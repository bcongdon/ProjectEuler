#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int sum_divisors(int x){
	int sum = 0;
	for(int i = 1; i < x; i++){
		if(x%i == 0){
			sum += i;
		}
	}
	return sum;
}

int main()
{
	bool abuntantNumber[28124] = {false};
	for(int i = 11; i < sizeof(abuntantNumber); i++){
		if(sum_divisors(i) >= i){
			abuntantNumber[i] = true;
		}
		else{
			abuntantNumber[i] = false;
		}
	}
	bool canBeSummed[28124] = {false};
	for(int a = 1; a < sizeof(canBeSummed); a++){
		for(int b = 1; b < sizeof(canBeSummed); b++){
			if(abuntantNumber[a] && abuntantNumber[b]){
				canBeSummed[a+b] = true;
				//cout << a+b << endl;
			}
		}
	}
	int sum = 0;
	for(int i = 0; i < sizeof(canBeSummed); i++){
		if(!canBeSummed[i]){
			cout << i << endl;
			sum += i;
		}
	}
	cout << sum << endl;
}