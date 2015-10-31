#include <iostream>
unsigned long largestPrimeFactor(unsigned long n){
	unsigned long largestFactor = 1;
	unsigned long p = 3;
	unsigned long div = n;

	while(div % 2 == 0){
		largestFactor = 2;
		div = div / 2;
	}
	while(div != 1){
		while(div % p == 0){
			largestFactor = p;
			div = div/p;
		}
		p += 2;
	}
	return largestFactor;
}

int main()
{
	int max = 100000;
	unsigned long factor;
	unsigned long i = 1;
	while(i <= max){
		factor = largestPrimeFactor(600851475143);
		i++;
	}
	std::cout << factor << std::endl;
}

