#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int i){
	// if(i%2==0 || i%5==0 || i%3==0){
	// 	return false;
	// }
	if(i<2){
		return false;
	}
	for(int j = 2; j < (int)std::sqrt(i) + 100; j++){
		if(i%j == 0 && i != j){
			return false;
		}
	}
	return true;
}

int main()
{
	unsigned long sum = 0;
	for(unsigned long i = 0; i < 2000000; i++){
		if(isPrime(i)){
			sum += i;
		}
		if(i % 10000 == 0){
			cout<< "Curr: " << i << endl;
		}
	}
	cout << sum << endl;
}