#include <iostream>

bool isPrime(int i){
	for(int j = 2; j < i; j++){
		if(i%j == 0 && i != j){
			return false;
		}
	}
	return true;
}

int main()
{
	int count = 0;
	int curr = 2;
	while(count < 10001){
		if(isPrime(curr)){
			count ++;
			//std::cout << "The " << count << " prime is " << curr << std::endl;
		}
		curr++;
	}
}