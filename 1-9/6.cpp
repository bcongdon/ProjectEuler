#include <iostream>
int main()
{
	unsigned long squares = 0;
	unsigned long sum = 0;
	for(unsigned long i = 1; i <= 100; i++){
		squares += i*i;
		sum += i;
	}
	sum *= sum;
	std::cout << (sum - squares) << std::endl;
}