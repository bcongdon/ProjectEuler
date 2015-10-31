#include <iostream>

int main()
{
	int sum = 2;
	int last = 2;
	int last2 = 1;
	int curr = 3;
	while(curr < 4000000){
		curr = last + last2;
		int temp = curr;
		last2 = last;
		last = temp;
		//std::cout << curr << std::endl;
		if(curr % 2 == 0){
			std::cout << curr << std::endl;
			sum += curr;
		}
	}
	std::cout << "Sum: " << sum << std::endl;
}