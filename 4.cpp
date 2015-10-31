#include <iostream>

bool isPalindrome(int test){
	int val = test;
	int orig = test;
	if(test < 10) return true;
	if(test % 10 == 0) return false;
	int reversed = 0;
	while(test >= 1){
		reversed = (reversed * 10) + (test % 10);
		test /= 10;
	}
	//std::cout << reversed << std::endl;
	if(reversed == orig) return true;
	else return false;
}

int main()
{
	int largestP = 0;
	for(int i = 0; i < 1000; i++){
		for(int j = 0; j < 1000; j++){
			if(isPalindrome(i*j) && i*j > largestP){
				largestP = i*j;
				std::cout << i << " * " << j << " = " << i*j << std::endl;
			}
		}
	}
}