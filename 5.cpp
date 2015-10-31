#include <iostream>
int main()
{
	bool numFound = false;
	int num = 21;
	while(numFound == false){
		numFound = true;
		for(int i = 1; i < 21; i++){
			if(num % i != 0){
				numFound = false;
				break;
			}
		}
		num++;
	}
	std::cout << num << std::endl;
}